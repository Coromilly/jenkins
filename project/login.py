import os
import mysql.connector
from mysql.connector import Error, connect

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("NAME"),
            passwd=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
