import model
import mysql.connector
from mysql.connector import errorcode

#Iniciate Database connection
try:
    cnn = mysql.connector.connect(
        user= 'root',
        password= '5460luis',
        host= 'localhost',
        database= 'utpWallet_Prod'        
        )
    # If connection success print message
    print ("\nSYSTEM MESSAGE : MYSQL DATABASE CONNECTED\n")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or Password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("DataBase does not exist")
    else:
        print(e)



# TEST GUI Request Variables
test_id = 1                       #TESTING VARIABLE: DECIDE WHO PASS THE CARD
topup_credit = 5.00               #TESTING VARIABLE: CREDIT
payment_debit = 2.00              #TESTING VARIABLE: DEBIT

# Filling Instance
handler = GET(test_id)
user_account = model.Card(
    handler[0],
    handler[1],
    handler[2],
    handler[3],
    handler[4],
    handler[5],
    handler[6])
# print (user_account.first_name)
# print(handler)


#Account Information Extraction
def GET(card_id):
    cursor = cnn.cursor()
    query = ('''SELECT acc_id,first_name,last_name,personal_id,acc_fac,b.career,acc_balance 
                    FROM usr_acc as a join career as b on a.acc_career = b.career_ID 
                    WHERE acc_id = %s''')
    cursor.execute(query,(card_id,))
    data=cursor.fetchone()
    cnn.commit() 
    cursor.close()
    return data

#Discount on account balance function
def Payment(account,debit):
    cursor = cnn.cursor()
    query1= ('''INSERT INTO trx VALUES(NULL,%s,1,NOW(),%s,0.00)''')
    cursor.execute(query1,(account.account_ID,debit,))
    cnn.commit() 
    
    new_balance = (float(account.current_balance) - debit)
    cursor = cnn.cursor()
    query2= ('''UPDATE usr_acc SET acc_balance=%s WHERE acc_id=%s''')
    cursor.execute(query2,(new_balance,account.account_ID,))
    cnn.commit()
    cursor.close()
    return 0

#Topup on account balance function
def Topup(account,credit):
    cursor = cnn.cursor()
    query1= ('''INSERT INTO trx VALUES(NULL,%s,2,NOW(),0.00,%s)''')
    cursor.execute(query1,(account.account_ID,credit,))
    cnn.commit() 
    
    new_balance = (float(account.current_balance) + credit)
    cursor = cnn.cursor()
    query2= ('''UPDATE usr_acc SET acc_balance=%s WHERE acc_id=%s''')
    cursor.execute(query2,(new_balance,account.account_ID,))
    cnn.commit()
    cursor.close()
    return 0

#Identification Extraction
def showInfo(account):
    name = account.first_name
    fam_name = account.last_name
    fac = account.faculty
    career = account.career
    return print("Name: "+name+" "+fam_name+"\nFaculty: "+fac+"\nCareer: "+career)

# Topup(user_account,topup_credit)
# Payment(user_account,payment_debit)
# showInfo(user_account)