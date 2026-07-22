import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sathwik@2004",
        database="library_management_system"
    )

    return connection
