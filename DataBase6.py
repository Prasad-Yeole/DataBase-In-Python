'''
Function Name    :  Create A New Table In The Database
Function Author  :  Prasad Yeole
Input            :  ----
Output           :  New Table Get Created

'''

import mysql.connector

def Create_Table():

    Connection = mysql.connector.connect(host = "localhost", database = "pythondb", user = "root", password = "")

    cobj = Connection.cursor()

    str1 = "drop table if exists studentdb"

    str2 = "create table studentdb(rollno int, name char(20), sex char(1), marks float)"

    try:
    
        cobj.execute(str1)
        cobj.execute(str2)
        print("Successfully Table Created...")

    except:

        Connection.rollback()
        print("Table Not Created")

    finally:

        cobj.close()
        Connection.close()

def main():

    Create_Table()

if __name__ == "__main__":
    main()

