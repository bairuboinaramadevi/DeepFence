#Common Functions
#File Functions
#Database functions
#Read/Write JSON configuration
#Read/Write prompts - get gemini code here
#event functions
from dotenv import load_dotenv
import os
import psycopg2
 
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(BASEDIR, '.env'))

def DBOperations(query, value ='', return_data = False, is_execute_many = False, return_columns=False):
    print("-------DBOperations Started Executing-------")
    connection = None
    cursor = None
    data = []
    columns = []
    try:
        connection = psycopg2.connect(
                    user = os.getenv('DB_USER'),
                    password = os.getenv('DB_PASSWORD'),
                    dbname = os.getenv('DB_NAME'),
                    host = os.getenv('DB_HOST'),
                    port = os.getenv('DB_PORT')
                )
        cursor = connection.cursor()
        if value == '':
            cursor.execute(query)
        elif is_execute_many and value != "":
            cursor.executemany(query, value)
        else:
            cursor.execute(query,value) 
        # print(query) 
        connection.commit()
        if query and (query.strip().lower().startswith('select') or query.strip().lower().startswith('with')) and return_data == False:
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                records = cursor.fetchall()
                # column can be used further converting in dataframe
                if return_columns:
                    return records, columns  # Explicitly returning both
                else:
                    # Default structure (as dicts with str values)
                    data = [dict(zip(columns, [str(val) for val in record])) for record in records]
                    return data
            else:
                return [] if not return_columns else ([], [])
        elif return_data: ## This condition is added for getting raw data like ids after inserting a record (as the ids are auto incremented)
            data = cursor.fetchall()
        else:
            data = {"status": "success"}
    except psycopg2.Error as db_error:
        print(f"Database error: {db_error}")
        data = {"status": 'failure' , "result": f"Database error: {db_error}"}
    except Exception as excep:
        data = {"status": 'failure','result':str(excep)}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    print("---> Response from DBOperation: ", data)
    return data
