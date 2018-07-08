__author__ = 'Luis Yao'

import mysql.connector
from mysql.connector import errorcode

def Database_connection():
    try:
        cnn = mysql.connector.connect(
            user= 'root',
            password= '5460luis',
            host= 'localhost',
            database= 'utpWallet_Prod'        
        )
        # If connection success print message
        print ("MySQL Server Connected")

    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with username or Password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("DataBase does not exist")
        else:
            print(e)
    
#create cursor 
    # cursor = cnn.cursor()

# testing query
    # query = ("SELECT * FROM USR_ACC")

#executing sql query
    # cursor.execute(query)

#printing
    # data=cursor.fetchall()
    # for row in data:
    #     print(row)

    # cnn.commit() 
    # cursor.close()
    # cnn.close