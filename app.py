import model
import mysql.connector
from mysql.connector import errorcode
from dbconnect import Database as MyDatabase
import pandas as pd
import matplotlib.pyplot as plt

# Calling the database connection
cnn = MyDatabase.connect_dbs()

# TEST GUI Request Variables
test_id = 1  # TESTING VARIABLE: DECIDE WHO PASS THE CARD
topup_credit = 666.25  # TESTING VARIABLE: CREDIT
payment_debit = 777.00  # TESTING VARIABLE: DEBIT

test_usr_id = 10
test_usr = "chombita123"  # TESTING OPERATIVE USER
test_pass = "1234"  # TESTING OPERATIVE PASSWORD

test_card_id = 6      # TESTING deleting card account id
test_fname = "Rosalina"       # TESTING first NAME
test_lname = "Mcpearson"       # TESTING last NAME
test_pid = "4-234-1234"       # TESTING personal ID 
test_fac = "FIC"       # TESTING faculty ID 
test_career = 2       # TESTING career code 
test_balance = 0.00       # TESTING initial balance 


# Account Validation
def acc_validation(card_ID):
    cursor = cnn.cursor()
    query = ('''SELECT acc_id FROM usr_acc WHERE acc_id = %s''')
    cursor.execute(query, (card_ID,))
    val = cursor.fetchone()
    if val is not None:
        return True
    else:
        return False
# Operative User Validation
def usr_validation(card_ID):
    cursor = cnn.cursor()
    query = ('''SELECT user_ID FROM user WHERE user_ID = %s''')
    cursor.execute(query, (card_ID,))
    val = cursor.fetchone()
    if val is not None:
        return True
    else:
        return False

# Account Enough Balance Validation
def balance_check(acc_owner, d_amount):
    cursor = cnn.cursor()
    query = ('''SELECT acc_balance FROM usr_acc WHERE acc_id = %s''')
    cursor.execute(query, (acc_owner.account_ID,))
    current_bal = cursor.fetchone()
    current_bal = current_bal[0]
    if(current_bal < d_amount):
        return False
    elif(current_bal > d_amount or current_bal == d_amount):
        return True

# Get account information for transaction
def get_acc(card_id):
    if (acc_validation(card_id)) == True:
        cursor = cnn.cursor()
        query = ('''SELECT acc_id,first_name,last_name,personal_id,acc_fac,b.career,acc_balance 
                        FROM usr_acc as a join career as b on a.acc_career = b.career_ID 
                        WHERE acc_id = %s''')
        cursor.execute(query, (card_id,))
        access_acc = cursor.fetchone()
        acc_info = model.Card(access_acc[0], access_acc[1], access_acc[2],
                              access_acc[3], access_acc[4], access_acc[5], access_acc[6])
        cnn.commit()
        cursor.close()
        return acc_info
    else:
        # print ("Account Error: Doesn't Exist")
        return False

# Operative User Authentification (Background Process)
def authenticate(log_account):
    cursor = cnn.cursor()
    query = ('''SELECT username FROM user WHERE username = %s''')
    cursor.execute(query, (log_account.username,))
    usr_data = cursor.fetchone()
    # usr_data = usr_data[0]
    if (usr_data is not None):
        usr_data = usr_data[0]
        query = ('''SELECT password FROM user WHERE username = %s''')
        cursor.execute(query, (usr_data,))
        pass_data = cursor.fetchone()
        pass_data = pass_data[0]
        if(log_account.password == pass_data):
            query = ('''SELECT usertype FROM user WHERE username = %s''')
            cursor.execute(query, (usr_data,))
            view_data = cursor.fetchone()
            view_data = view_data[0]
            log_account.type = view_data
            return log_account
        else:
            # print("SYSTEM INFO: Password Incorrect")
            return False
    else:
        return False

# Operative User Sign In
def sign_in(input_user, input_pass):
    operator = model.User(input_user, input_pass)
    current_user = authenticate(operator)

    return current_user
        # print("SYSTEM INFO: Error - Username or Password doesnt't match or doesn't Exist")

# Adding operative user
def new_user(n_username,n_password,type):
    cursor = cnn.cursor()
    query = ('''SELECT * FROM user WHERE username = %s''')
    cursor.execute(query, (n_username,))
    val = cursor.fetchone()
    if val is not None:
        # return print("SYSTEM ERROR: Username already exist")
        return False
    else:
        new_usr = model.User(n_username,n_password)
        new_usr.user_type = type
        cursor = cnn.cursor()
        query1 = ('''INSERT INTO user VALUES(NULL,%s,%s,%s)''')
        cursor.execute(query1, (new_usr.username, new_usr.password,new_usr.user_type,))
        cnn.commit()
        print("SYSTEM INFO: New user created successfully")
        return True
        
# Deleting operative user
def del_user(ex_usr_id):
    if (usr_validation(ex_usr_id)) == True:
        cursor = cnn.cursor()
        query = ('''DELETE FROM user WHERE user_id = %s''')
        cursor.execute(query, (ex_usr_id,))
        cnn.commit()
        cursor.close()
        print("SYSTEM INFO: User with ID",ex_usr_id,"deleted successfully")
    else:
        print("SYSTEM ERROR: User doesn't exist")
    return 0

# Adding Card Accounts
def new_card(n_fname,n_lname,n_pid,n_acc_fac,n_acc_career,n_acc_balance):
    cursor = cnn.cursor()
    query = ('''SELECT * FROM usr_acc WHERE personal_id = %s''')
    cursor.execute(query, (n_pid,))
    val = cursor.fetchone()
    if val is not None:
        return print("SYSTEM ERROR: Account already exist")
    else:
        new_acc = model.Card(0,n_fname,n_lname,n_pid,n_acc_fac,n_acc_career,n_acc_balance)
        cursor = cnn.cursor()
        query1 = ('''INSERT INTO usr_acc VALUES(NULL,%s,%s,%s,%s,%s,%s)''')
        cursor.execute(query1, (new_acc.first_name,
                                new_acc.last_name,
                                new_acc.personal_ID,
                                new_acc.faculty, 
                                new_acc.career,
                                new_acc.current_balance,))
        cnn.commit()
        print("SYSTEM INFO: New Card Account created successfully")
        return 0
        
# Deleting Card Accounts
def del_card(ex_card_id):
    if (acc_validation(ex_card_id)) == True:
        cursor = cnn.cursor()
        query = ('''DELETE FROM usr_acc WHERE acc_ID = %s''')
        cursor.execute(query, (ex_card_id,))
        cnn.commit()
        cursor.close()
        print("SYSTEM INFO: Card Account with ID",ex_card_id,"deleted successfully")
    else:
        print("SYSTEM ERROR: Card Account doesn't exist")
    return 0
        

# Discount on account balance function
def Payment(account, debit):
    if(balance_check(account, debit)) == True:
        cursor = cnn.cursor()
        query1 = ('''INSERT INTO trx VALUES(NULL,%s,1,CURDATE(),%s,0.00)''')
        cursor.execute(query1, (account.account_ID, debit,))
        cnn.commit()

        new_balance = (float(account.current_balance) - debit)
        cursor = cnn.cursor()
        query2 = ('''UPDATE usr_acc SET acc_balance=%s WHERE acc_id=%s''')
        cursor.execute(query2, (new_balance, account.account_ID,))
        cnn.commit()
        cursor.close()
        return print("Payment Transaction Successfully Done\n ${0:.2f} deducted from your account".format(debit))
    else:
        return print("Payment Error: Not Enough Money")

# Topup on account balance function
def Topup(account, credit):
    if(account != False):
        cursor = cnn.cursor()
        query1 = ('''INSERT INTO trx VALUES(NULL,%s,2,CURDATE(),0.00,%s)''')
        cursor.execute(query1, (account.account_ID, credit,))
        cnn.commit()

        new_balance = (float(account.current_balance) + credit)
        cursor = cnn.cursor()
        query2 = ('''UPDATE usr_acc SET acc_balance=%s WHERE acc_id=%s''')
        cursor.execute(query2, (new_balance, account.account_ID,))
        cnn.commit()
        cursor.close()
        return print("Top-up Transaction Successfully Done\n ${0:.2f} added to your account".format(credit))
    else:
        return print("Top-up Error: Account Doesn't Exist.")

# Identification Extraction
def showInfo(account):
    if(account != False):
        name = account.first_name
        fam_name = account.last_name
        fac = account.faculty
        career = account.career
        return account
    else:
        # return print("Indentification Error: Account not in database")
        return False

def dataAnalysis():
    cursor = cnn.cursor()
    myFrames = pd.read_sql_query('''SELECT date,sum(debit) as debit,sum(credit) as credit FROM trx GROUP BY date''', cnn)
    S_date = pd.Series(myFrames.date)
    S_debit = pd.Series(myFrames.debit)
    S_credit = pd.Series(myFrames.credit)
    dataframe = pd.concat([S_date,S_debit,S_credit],axis=1)     #Dataframe
    dataframe.columns = ['Date','Debit','Credit']
    # dataframe.set_index('Date',inplace=True,drop=True)
    dataframe.plot(x="Date", y=["Debit", "Credit"],kind='bar')
    # S_credit.plot(grid=True)
    plt.show()
    print(dataframe)



# Topup(get_acc(test_id),topup_credit)
# Payment(get_acc(test_id),payment_debit)
# showInfo(get_acc(test_id))
# sign_in(test_usr, test_pass)
# new_user(test_usr,test_pass,test_type)
# del_user(test_usr_id)
# new_card(test_fname,test_lname,test_pid,test_fac,test_career,test_balance)
# del_card(test_card_id)
dataAnalysis()