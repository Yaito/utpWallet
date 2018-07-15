import mysql.connector
from mysql.connector import errorcode

class Database:
    '''This class is used to initialize the connection to the MySQL Database'''
    @staticmethod
    def connect_dbs():
        try:
            cnn = mysql.connector.connect(
                user='root',
                password='utpadmin',
                host='localhost',
                database='utpWallet_Prod')
            # If connection success print message
            print("\nSYSTEM MESSAGE : MYSQL DATABASE CONNECTED\n")
            return cnn
            
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with username or Password")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("DataBase does not exist")
            else:
                print(e)