import psycopg2 as pg
import json
from connect import connection as conn

def lambda_function(event):

    # db connectivity check
    # if conn:
    #     cursor = conn.cursor()
    #     conn.autocommit = True
    #     print("Successfully connected to database")
    # else:
    #     print('Please check db credentials')
    
    cursor = conn.cursor() 

    #main function body
    car_id = event["id"]
    dbqry = f"SELECT car_id, car_name, car_engine FROM public.cars where car_id = {car_id} ;"
    cursor.execute(dbqry)
    columns = [desc[0] for desc in cursor.description]
    qryres = [dict(zip(columns,row)) for row in cursor.fetchall()]
           
    return json.dumps(qryres)

event = { 'id' : 2 }
print(lambda_function(event))


{
    'id' : 3,
    'car_name' : 'Jaguar XC700',
    'car_engine' : 'MVT234591C18'
}