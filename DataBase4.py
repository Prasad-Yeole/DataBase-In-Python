'''
Function Name    :  Delete A Record From emptab
Function Author  :  Prasad Yeole
Input            :  Int
Output           :  Record Get Deleted From The Row

'''

import mysql.connector

def Delete_Rows(Name):

    Connction = mysql.connector.connect(host = "localhost", database = "Unbrand", user = "root", password = "")

    cobj = Connction.cursor()

    str = "delete from Info where Name = '%s' "

    value = (Name)

    try:

        cobj.execute(str % value)
        Connction.commit()
        
        print("Row Deleted...")

    except:

        Connction.rollback()
        print("Not Deleted")

    finally:

        cobj.close()
        Connction.close()

def main():

    Name = input("Enter The Name : ")

    Delete_Rows()

if __name__ == "__main__":
    main()
