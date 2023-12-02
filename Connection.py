'''
Function Name    :  Display All Rows From Employee Table
Function Author  :  Prasad Yeole
Input            :  ----
Output           :  It Display All Records Of Info Table

'''

import mysql.connector

def connect_to_DataBase():
    try:
        # Replace these values with your DataBase connection details
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Unbrand"
        )

        if connection.is_connected():
            print("Connected to DataBase")
            
            # Perform database operations here
            
            # Example: Execute a simple query
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM produt_dtls")
            rows = cursor.fetchall()

            for row in rows:
                print(row)

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    connect_to_DataBase()
