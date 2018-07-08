class Card(object):
    def __init__(self,acc_id,fname,lname,per_id,faculty,career,balance):
        self.account_ID = acc_id
        self.first_name = fname
        self.last_name = lname
        self.personal_ID = per_id
        self.faculty = faculty
        self.career = career
        self.current_balance = balance
        
# Testing model
# card_one = Card(5,'luis','yao','22-2232-23','fisc','sistema','223.23')
# card_one.first_name = 'roderick'
# print(card_one.first_name)
