'''
Function Name    :  Display All Rows From Employee Table
Function Author  :  Prasad Yeole
Input            :  ----
Output           :  It Display All Records Of Emptab

'''

import mysql.connector

def Connection():
    
    Connection = mysql.connector.connect(host = "localhost", database = "Unbrand", user = "root", password = "")

    cobj = Connection.cursor()
    cobj.execute("select * from Info")

    '''row = cobj.fetchone()
                                  OR
    while row != None:
        print(row)
        row = cobj.fetchone()'''

    rows = cobj.fetchall()
    
    print("Total Number of Rows are : ", cobj.rowcount)

    for row in rows:
        print(row)

    cobj.close()
    Connection.close()

def main():
    
    Connection()

if __name__ == "__main__":
    main()
