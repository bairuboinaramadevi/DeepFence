import json
import os.path
from datetime import date, datetime
from flask import jsonify
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os
import psycopg2
import queue
import threading
import time
from socket_io_setup import socketio
 
def paramsFilling(Workflow,EventTypeID, EventDescription, EventData, ObjectID,ChangeWorkflow=False):
    telemetryObj = {
        "Workflow":Workflow,
        "UserID": 1,
        "EventSourceID": 2,
        "EventTypeID": EventTypeID,
        "EventDescription": EventDescription,
        "EventData": EventData,
        "ObjectID": ObjectID
    }

    dbparams = {
        "queryType": "insert",
        "TelemetryObj": telemetryObj
    }
    socketio.emit(f'AgentExecuted', json.dumps(telemetryObj))
    if ChangeWorkflow:
        socketio.emit(f'WorkflowCompleted', "Workflow Completed")
    ManageTelemetry(dbparams)
    return "Working"

worker_thread_running = False

event_queue = queue.Queue()

load_dotenv('.env')

def ManageTelemetry(db_params):
    print("ManageTelemetry->",db_params)
    #Declare a variable called query_type and assign it the value of the queryType key in the db_params dictionary
    query_type = db_params['queryType']
    #Declare an empty list called data
    data = []
    #Declare a variable called connection and assign it the result of a psycopg2 connection using the parameters of the environment variables DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, and DB_PORT
    connection = psycopg2.connect(
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            dbname = os.getenv('DB_NAME'),
            host = os.getenv('DB_HOST'),
            port = os.getenv('DB_PORT')
        )
    #Declare a variable called cursor and assign it the result of a psycopg2 cursor using the connection variable
    cursor = connection.cursor()
    global worker_thread_running
    #If the query_type is equal to "insert"
    if query_type == "insert":
        #Declare a variable called telemetry_obj and assign it the value of the telemetryObj key in the db_params dictionary
        telemetry_obj = db_params['TelemetryObj']

        event_queue.put(telemetry_obj)
        
        # to trigged once when there the queue was empty,
        if not worker_thread_running and not event_queue.empty():
            worker_thread = threading.Thread(target=__InsertEnqueuedEvent)
            worker_thread.daemon = True  # Allow the main thread to exit even if the worker is still running
            worker_thread.start()

    elif query_type == "EventTypeId":
        event = db_params["Event"]
        #Declare an empty list called data
        query = f"""SELECT * FROM "Telemetry"."EventType"  WHERE "Event" = '{event}'"""
        cursor.execute(query)
        #Declare a variable called columns and assign it the result of a list comprehension that creates a list of the column names from the cursor description
        columns = [desc[0] for desc in cursor.description]
        #Declare a variable called records and assign it the result of the cursor.fetchall() method
        records = cursor.fetchall()
        #Loop through the records
        for record in records:
            #Declare a variable called tcrow and assign it a list of the row values from the record
            tcrow=[str(rowval) for rowval in record]
            #Append a dictionary of the column and row values to the data list
            data.append(dict(zip(columns, tcrow)))  

    #If the query_type is equal to "read"
    elif query_type == "read":
        limit = db_params['limit']
        telemetry_obj = db_params['TelemetryObj']
        #Execute a query using the cursor variable to select the RoleName column from the Role table
        fetch_query = ""
        if limit == "0":
            fetch_query = f"""SELECT * FROM (SELECT * FROM "Telemetry"."Event" ev INNER JOIN "Telemetry"."EventSource" evs 
                ON "ev"."EventSourceID" = "evs"."EventSourceID" WHERE "ev"."EventSourceID" = '{telemetry_obj["EventSourceID"]}') evevs INNER JOIN "Telemetry"."EventType" evt ON "evevs"."EventTypeID" = "evt"."EventTypeID" WHERE "evevs"."UserID" = '{telemetry_obj["UserID"]}' ORDER BY "evevs"."Timestamp" DESC;"""

        else:
            fetch_query = f"""SELECT * FROM (SELECT * FROM "Telemetry"."Event" ev INNER JOIN "Telemetry"."EventSource" evs 
                ON "ev"."EventSourceID" = "evs"."EventSourceID" WHERE "ev"."EventSourceID" = '{telemetry_obj["EventSourceID"]}') evevs INNER JOIN "Telemetry"."EventType" evt ON "evevs"."EventTypeID" = "evt"."EventTypeID" WHERE "evevs"."UserID" = '{telemetry_obj["UserID"]}' ORDER BY "evevs"."Timestamp" DESC LIMIT 3;"""

        cursor.execute(fetch_query)
        #Declare a variable called columns and assign it the result of a list comprehension that creates a list of the column names from the cursor
        columns = [desc[0] for desc in cursor.description]
        #Declare a variable called records and assign it the result of a list comprehension that creates a list of the records from the cursor
        records = cursor.fetchall()
        #Iterate through the records and append each record to the data list
        for record in records:
              tcrow=[str(rowval) for rowval in record]
              data.append(dict(zip(columns, tcrow))) 

    #Close the cursor and connection variables
    cursor.close()
    connection.close()
    #Return the data list as a JSON string with indentation of 4 spaces
    return json.dumps(data,indent=4)


def __InsertEnqueuedEvent():
    global worker_thread_running
    worker_thread_running = True
    #Declare a variable called query and assign it a string containing an SQL query
    #Declare a variable called connection and assign it the result of a psycopg2 connection using the parameters of the environment variables DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, and DB_PORT
    connection = psycopg2.connect(
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            dbname = os.getenv('DB_NAME'),
            host = os.getenv('DB_HOST'),
            port = os.getenv('DB_PORT')
        )
    #Declare a variable called cursor and assign it the result of a psycopg2 cursor using the connection variable
    cursor = connection.cursor()
    while not event_queue.empty():        
        time.sleep(0.5)        
        # convert to string
        
        try:
            telemetry_obj = event_queue.get()
            
            now = datetime.now()
            date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            telemetry_obj["Timestamp"] = date_time_str
            if telemetry_obj["ObjectID"] == None:
                query = f'INSERT INTO "Telemetry"."Event" (\"Timestamp\", \"EventSourceID\", \"EventTypeID\", \"UserID\", \"EventDescription\",\"EventData\") VALUES (%(Timestamp)s,%(EventSourceID)s, %(EventTypeID)s, %(UserID)s, %(EventDescription)s,%(EventData)s);' 
                #Execute the query using the cursor variable and the feedback_obj variable as parameters
                cursor.execute(query,telemetry_obj)
            else:
                query = f'INSERT INTO "Telemetry"."Event" (\"Timestamp\", \"EventSourceID\", \"EventTypeID\",\"ObjectID\", \"UserID\", \"EventDescription\",\"EventData\") VALUES (%(Timestamp)s,%(EventSourceID)s, %(EventTypeID)s, %(ObjectID)s, %(UserID)s, %(EventDescription)s,%(EventData)s);' 
                #Execute the query using the cursor variable and the feedback_obj variable as parameters
                cursor.execute(query,telemetry_obj)
            #Commit the changes to the database
            connection.commit()
            event_queue.task_done()
        except queue.Empty:
            break
        except Exception as exc:
            print(exc)
            connection.rollback()
    worker_thread_running = False