'''
Function Name    :  Insert One Record Into emptab
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Record Get Inserted Into The Row

'''

import mysql.connector

def insert_record(name, age):
	try :

		connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "Unbrand")

		if connection.is_connected():

			cursor = connection.cursor();

			qurey = "insert into Info(name, age) values (%s,%s)"
			record_data = (name,age)
			cursor.execute(qurey,record_data)
			connection.commit()

	except mysql.connector.Error as e:
		print(f"Error {e}")

	finally:
		if 	connection.is_connected():
			cursor.close()
			connection.close()
			print("connection is closed.")

def main():
	insert_record("sai",12)


if __name__ == "__main__":
	main()
