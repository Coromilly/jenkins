import json
import mysql.connector
from mysql.connector import Error, connect

def get_login_info(file):
    with open (file, 'r') as f:
        data_json = json.loads(f.read())
        host_name = data_json['host_name']
        user_name = data_json['user_name']
        user_password = data_json['user_password']
        db_name = data_json['database_name']
        return host_name, user_name, user_password, db_name


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
