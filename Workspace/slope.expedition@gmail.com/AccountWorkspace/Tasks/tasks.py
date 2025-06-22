from celery import shared_task
from time import sleep
from celery.utils.log import get_task_logger
import logging
import json
from datetime import timedelta
from celery.signals import after_setup_logger
from sqlalchemy import insert
from datetime import datetime
logger = logging.getLogger(__name__)
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///celerySql.db', echo = True)
meta = MetaData()
conn = engine.connect()
Jobs = Table(
   'Jobs', meta, 
   Column('id', Integer, primary_key = True), 
   Column('TaskName', String), 
   Column('Result', Integer),
)
meta.create_all(engine) 
import psycopg2
import random
data = []
@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add filehandler
    fh = logging.FileHandler('celery.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
import json


@shared_task()
def create_schedule(*args, **kwargs):
    connection = psycopg2.connect(
         database="postgres", 
         user='postgres', 
         password='postgres', 
         host='127.0.0.1',
         port="5432")
    cursor = connection.cursor()
    taskList = ['sum_func','multiply_func','div_func','min_func']
    frequencyList = ["One Time", "Daily", "Weekly", "Monthly"]
    taskName= random.choice(taskList)
    num1 = random.randint(1, 100)
    num2 = random.randint(100, 200)
    p = {"a":num1,"b":num2}
    f = random.choice(frequencyList)  
    n = random.randint(1, 10)        
    date1 = datetime.now()+ timedelta(minutes=n)
    postgres_insert_query =f'INSERT INTO "TaskScheduler"."Schedule" (\"Name\", \"Frequency\",\"StartDateTime\" ,\"Parameters\") VALUES  (%s, %s, %s,%s);'
    values = (taskName,f,date1,json.dumps(p))
    cursor.execute(postgres_insert_query,values)
    connection.commit()
    count = cursor.rowcount
    print(date1)
    print(count, "Record inserted successfully into schedule table")
    return date1

@shared_task()
def store_result_telemetry(*args, **kwargs):
    data = []
    connection = psycopg2.connect(
         database="postgres", 
         user='postgres', 
         password='postgres', 
         host='127.0.0.1',
         port="5432")
    cursor = connection.cursor()
    cursor.execute('SELECT "ID", "Name", "Parameters" ->> \'a\' AS num1, "Parameters" ->> \'b\' as num2, "Frequency", "StartDateTime" FROM "TaskScheduler"."Schedule"  WHERE "StartDateTime">= NOW() and "StartDateTime"<= NOW()+INTERVAL \'5 minutes\'')
    columns = [desc[0] for desc in cursor.description]
    records = cursor.fetchall()
    for record in records:
         tcrow=[str(rowval) for rowval in record]
         d=dict(zip(columns, tcrow))
         data.append(d)    
    date = datetime.now()
    for x in data:
        TaskName = x.get('Name')
        num1 = x.get('num1')
        num2 =x.get('num2')
        if(TaskName=="sum_func"):
            ans = sum_func(int(num1),int(num2))
        elif(TaskName=="multiply_func"):
            ans = multiply_func(int(num1),int(num2))
        elif(TaskName=="div_func"):
            ans = div_func(int(num1),int(num2))
        else:
            ans = min_func(int(num1),int(num2))     
        postgres_query =f'INSERT INTO "TaskScheduler"."Telemetry" (\"DateTime\", \"Output\",\"TaskName\") VALUES  (%s, %s, %s);'
        values = (date,ans,TaskName)
        cursor.execute(postgres_query,values)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into Telemetry table")
    
    cursor.close()
    connection.close()
    return data


@shared_task()
def read_from_telemetry(*args, **kwargs):
    data = []
    connection = psycopg2.connect(
         database="postgres", 
         user='postgres', 
         password='postgres', 
         host='127.0.0.1',
         port="5432")
    cursor = connection.cursor()
    cursor.execute('SELECT "ID", "DateTime", "Output", "TaskName" FROM "TaskScheduler"."Telemetry"')
    columns = [desc[0] for desc in cursor.description]
    records = cursor.fetchall()
    for record in records:
         tcrow=[str(rowval) for rowval in record]
         d=dict(zip(columns, tcrow))
         data.append(d)    

    cursor.close()
    connection.close()
    return data
@shared_task()
def read_from_Schedule(*args, **kwargs):
    data = []
    connection = psycopg2.connect(
         database="postgres", 
         user='postgres', 
         password='postgres', 
         host='127.0.0.1',
         port="5432")
    cursor = connection.cursor()
    cursor.execute('SELECT "ID", "Name", "Parameters", "Frequency", "StartTime", "EndTime" FROM "TaskScheduler"."Schedule"')
    columns = [desc[0] for desc in cursor.description]
    records = cursor.fetchall()
    for record in records:
         tcrow=[str(rowval) for rowval in record]#values without columnNames
         #print(str(tcrow[5]).split(":"))
         #print("tcrow %s" %str(tcrow))
         d=dict(zip(columns, tcrow))#values without columnNames
         #print("d %s" %str(d))
         data.append(d)    

    cursor.close()
    connection.close()
    return data


@shared_task()
def sum_func(a, b, *args, **kwargs):
    print("Task1: Started")
    logger.info("started")
    r = a+b
    stmt = insert(Jobs).values(TaskName='Task1:ADD NUMBERS', Result=r)
    # stmt.compile()
    with engine.connect() as conn:
        
        conn.execute(stmt)
        #conn.commit()
    return r

print(sum_func(10,20))
@shared_task()
def sub_func(a, b, *args, **kwargs):
    print("Task2: Started")
    #sleep(2)
    result = a-b
    stmt = insert(Jobs).values(TaskName='Task2:SUB NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task2: Ended")
    return result
print(sub_func(100,20))
@shared_task()
def multiply_func(a, b, *args, **kwargs):
    print("Task3: Started")
    #sleep(2)
    result = a*b
    stmt = insert(Jobs).values(TaskName='Task3:MULTIPLY NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        ##conn.commit()
    print("Task3: Ended")
    return result

@shared_task()
def div_func(a, b, *args, **kwargs):
    print("Task4: Started")
    #sleep(2)
    result = a/b
    stmt = insert(Jobs).values(TaskName='Task4:DIV NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task4: Ended")
    return result

@shared_task()
def mod_func(a, b, *args, **kwargs):
    print("Task5: Started")
    #sleep(2)
    result = a%b
    stmt = insert(Jobs).values(TaskName='Task5:MOD NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task5: Ended")
    return result

@shared_task()
def min_func(a, b, *args, **kwargs):
    print("Task6: Started")
    #sleep(2)
    result = min(a, b)
    stmt = insert(Jobs).values(TaskName='Task6:MIN NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task6: Ended")
    return result

@shared_task()
def max_func(a, b, *args, **kwargs):
    print("Task7: Started")
    #sleep(2)
    result = max(a, b)
    stmt = insert(Jobs).values(TaskName='Task7:MAX NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task7: Ended")
    return result

@shared_task()
def avg_func(a, b, *args, **kwargs):
    print("Task8 Started")
    #sleep(2)
    result = (a+b)/2
    stmt = insert(Jobs).values(TaskName='Task8:AVG NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task8: Ended")
    return result

@shared_task()
def pow_func(a, b, *args, **kwargs):
    print("Task9: Started")
    #sleep(2)
    result = pow(a, b)
    stmt = insert(Jobs).values(TaskName='Task9:POW NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task9: Ended")
    return result

@shared_task()
def sumsquare_func(a, b, *args, **kwargs):
    print("Task10: Started")
    #sleep(2)
    result=(a+b)**2
    stmt = insert(Jobs).values(TaskName='Task10:SUMSQUARE NUMBERS', Result=result)
    stmt.compile()
    with engine.connect() as conn:
        conn.execute(stmt)
        #conn.commit()
    print("Task10: Ended")
    return result





