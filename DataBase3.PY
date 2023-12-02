'''
Function Name    :  Insert Multiple Records Into emptab
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Record Get Inserted Into The Row

'''

import mysql.connector

def insertRecord(Name, Age):

	try:
		connection = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "Unbrand")
		
		if connection.is_connected():
			print("Connection established")

			cursor = connection.cursor();

			query = "insert into Info(Name,Age) values ('%s','%d')"
			data = (Name,Age)

			cursor.execute(query % data)

			connection.commit()

			print("Succesfully Entered")
	except mysql.connector.Error as e:
		print(f"Error {e}")

	finally:
		if connection.is_connected():
			cursor.close()
			connection.close()
		print("Program Succesfully excuted")



def main():

	iNo = int(input("How many record you want to Enter : "));

	for _ in range(iNo):

		Name = input("Enter the name : ")
		Age = int(input("enter the age : "))

		insertRecord(Name,Age)




if __name__ == '__main__':
	main()