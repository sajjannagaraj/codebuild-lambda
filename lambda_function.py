import json
import pandas as pd
# The Snowflake Connector library.
import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas
## Phase I: Setup and Connect
# The connector...
#aws-private-link


def lambda_handler(event, context):
    # TODO implement
    

    try:
        
        # read SQL file
        ddl_file = open('ddls.txt', 'r')
        sql_file = ddl_file.read()
        ddl_file.close()
        sql_commands = sql_file.split(';')
        
        conn = snow.connect(user="shasgund",
        password="Srav_123",
        account="dxa10182.us-east-1",
                        )
                        
        # Creating a cursor object
        cur = conn.cursor()
        print("Cursor object Create !")
        sql = "USE ROLE SYSADMIN"
        cur.execute(sql)
        
        sql = "USE DATABASE POC"
        cur.execute(sql)
        sql = "USE SCHEMA PUBLIC"
        cur.execute(sql)
        
        print("Query Executing")
        for command in sql_commands:
            print(command)
            print(cur.execute(command))
            
        print("Query Executed!")
        
        # sql = "CREATE TABLE PartyType4(PartyType INTEGER NOT NULL ,PartyTypeName VARCHAR(20) NULL ,PartyTypeStatus VARCHAR(20) NULL ,PartyTypeDescription VARCHAR(20) NULL);"
        # cur.execute(sql)
        
        # print("Query1 Executed!")
        # sql = "CREATE TABLE Party4(PartyID INTEGER NOT NULL ,PartyName VARCHAR(20) NULL ,PartyDescription VARCHAR(20) NULL ,PartyType INTEGER NOT NULL ,PartyStatus boolean NULL);"
        # cur.execute(sql)
        # print("Query2 Executed!")
        
        cur = conn.cursor()
        return {
            'statusCode': 200,
            'body': json.dumps('Code Executed!')
        }
        
    
    except Exception as e:
        print(e)