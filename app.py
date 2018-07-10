import model
import mysql.connector
from mysql.connector import errorcode

# Iniciate Database connection
try:
    cnn = mysql.connector.connect(
        user='root',
        password='5460luis',
        host='localhost',
        database='utpWallet_Prod'
    )
    # If connection success print message
    print("\nSYSTEM MESSAGE : MYSQL DATABASE CONNECTED\n")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or Password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("DataBase does not exist")
    else:
        print(e)

# TEST GUI Request Variables
test_id = 1  # TESTING VARIABLE: DECIDE WHO PASS THE CARD
topup_credit = 1235.75  # TESTING VARIABLE: CREDIT
payment_debit = 1000.00  # TESTING VARIABLE: DEBIT

test_usr = "chombi1234"  # TESTING OPERATIVE USER
test_pass = "1234"  # TESTING OPERATIVE PASSWORD

# Account Validation
def acc_validation(test_id):
    cursor = cnn.cursor()
    query = ('''SELECT acc_id FROM usr_acc WHERE acc_id = %s''')
    cursor.execute(query, (test_id,))
    val = cursor.fetchone()
    if val is not None:
        return True
    else:
        return False
# print(acc_validation(get_acc(test_id)))

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
# print(get_acc(test_id))

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
    if current_user is not False:
        if(current_user.type == 1):
            ####
            print("SYSTEM INFO: Successfully Logged in")
            print("Type 1 - Admin")
        elif(current_user.type == 2):
            ###
            print("SYSTEM INFO: Successfully Logged in")
            print("Type 2 - Admin")
        elif(current_user.type == 3):
            ###
            print("SYSTEM INFO: Successfully Logged in")
            print("Type 3 - Admin")
    else:
        print("SYSTEM INFO: Error - Username or Password doesnt't match or doesn't Exist")


# Discount on account balance function
def Payment(account, debit):
    if(balance_check(account, debit)) == True:
        cursor = cnn.cursor()
        query1 = ('''INSERT INTO trx VALUES(NULL,%s,1,NOW(),%s,0.00)''')
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
        query1 = ('''INSERT INTO trx VALUES(NULL,%s,2,NOW(),0.00,%s)''')
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
        return print("Name: "+name+" "+fam_name+"\nFaculty: "+fac+"\nCareer: "+career)
    else:
        return print("Indentification Error: Account not in database")


# Topup(get_acc(test_id),topup_credit)
# Payment(get_acc(test_id),payment_debit)
# showInfo(get_acc(test_id))
sign_in(test_usr, test_pass)
