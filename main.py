__author__ = "spark expedition"
__copyright__ = "Copyright 2023, UnFold"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "spark expedition"
__email__ = "spark.expedition@gmail.com"
__status__ = "Development"

import os

from flask import jsonify
from flask import render_template,  json
from flask_cors import CORS
from flask import Flask
import logging

import os
import os

import psycopg2

from WorkflowAgents.execute import run_agents
from static.CommonFunctions import DBOperations
# from flask_socketio import SocketIO
# # import asyncio
# # from asyncio import WindowsSelectorEventLoopPolicy

# # asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

app = Flask(__name__)
# socketio = SocketIO(app)

from socket_io_setup import socketio
socketio.init_app(app, cors_allowed_origins="*")
# socketio = SocketIO(app, cors_allowed_origins="*", allow_EIO3=True)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['model'] = ""
app.config['mname'] = ""
app.config['vname'] = ""

# Create a global logger object
logger = logging.getLogger(__name__)

# Configure the logger to use Stackdriver Logging
# You can also set the logging level and format if needed
logging.basicConfig(level=logging.INFO)


@app.route("/execute_agents", methods=["GET"])
async def execute_agents_route():
    """Asynchronous route to execute agents."""
    results = await run_agents()  # Correctly await the async function
    return jsonify(results)

@app.route("/AgenticWorkflow")
def AgenticWorkflow():  
  return render_template('AgenticWorkflow.html')

@app.route("/AgentOrchestration")
def AgentOrchestration():  
  return render_template('AgentOrchestration.html')

@app.route("/AgentDashboard")
def AgentDashboard():  
  return render_template('AgentDashboard.html')

@app.route("/FetchFromDatabase")
def FetchFromDatabase():
    data = []
    json_records = {}
    try:
        query1 = """SELECT
                    "EventData"->>'Status' AS eventstatus,
                    COUNT("EventTypeID") AS Count
                      FROM
                          "Telemetry"."Event"
                      WHERE
                          "EventTypeID" >= 13000
                      GROUP BY
                          "EventData"->>'Status'"""
        
        query2="""SELECT
                te."Feature",
                COUNT(t."EventTypeID") AS count
                FROM "Telemetry"."Event" AS t
                JOIN "Telemetry"."EventType" AS te
                  ON t."EventTypeID" = te."EventTypeID"
                WHERE
                  t."EventTypeID" >= 13000
                GROUP BY
                  te."Feature"
              """
        EventStatus = DBOperations(query1)
        EventStatus = {item['eventstatus']: int(item['count']) for item in EventStatus}
        EventLog=DBOperations(query2)
        # EventLog = [{item['Feature']: int(item['count'])} for item in EventLog]
        for item in EventLog:
          item['count'] = int(item['count'])
        return {"EventStatus":EventStatus,"EventLog":EventLog}
        return json.loads(json.dumps(data, indent=4))
    except (Exception, psycopg2.Error) as error:
        print("Error fetching records from PostgreSQL: ", error)
        return {"message": "Error fetching records from PostgreSQL: " + error}
    finally:        
        print("PostgreSQL connection closed.")

if __name__ == '__main__':
    # app.run(debug=True,port=5005)
    # mlflow_process.terminate()
    app.run(host='0.0.0.0',port=5505,debug=False)
    # socketio.run(app,port=5005,debug=True)
