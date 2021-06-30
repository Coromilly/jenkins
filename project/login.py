import sys
import mysql.connector
from mysql.connector import Error, connect

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=sys.argv[1],
            user=sys.argv[2],
            passwd=sys.argv[3],
            database=sys.argv[4]
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
