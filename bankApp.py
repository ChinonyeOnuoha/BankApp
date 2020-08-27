### BASIC UP TO GENERATE

# import random

# class User:

#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):

   

#     def __init__(self, name, age, email, phone):  ## Initialize child class
#         super().__init__(name, age, email, phone)  ## Initialize attributes from parent class
#         self.balance = 0
#         self.account_no = self.generate_acct_no()
    
#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3999999999)
#         return str(account_num)

# x = Account('atha', 23, 'nonye_mg@yahoo.com', '08032134387')
# print(x.account_no)


#--------------------------------------------------------------------------------------------------------------------------------------------------

# import random
# import locale

# class User:

#     def __init__(self, name, age, email, phone):

#         self.name = name
#         self.age = age
#         self.email = email
#         self.phone = phone

# class Account(User):

   

#     def __init__(self, name, age, email, phone):  ## Initialize child class
#         super().__init__(name, age, email, phone)  ## Initialize attributes from parent class
#         self.balance = 0
#         self.account_no = self.generate_acct_no()

#     ## METHODS
#     def generate_acct_no(self):

#         account_num = random.randint(3000000000, 3999999999)
#         return str(account_num)

#     ## DEPOSIT
#     def deposit(self, amount, comment = ''):

#         amount = amount.replace(",", "")

#         self.balance += int(amount)                               ## Adds deposit value to balance

        
#         locale.setlocale(locale.LC_ALL, 'en_US')
#         str_balance = locale.format_string("%d", self.balance, grouping=True)

#         print(f'Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{str_balance} ')


#     ##WITHDRAW
#     def withdraw(self, amount, comment = ''):

#         amount = amount.replace(",", "")

#         self.balance -= int(amount)                               ## Adds deposit value to balance

        
#         locale.setlocale(locale.LC_ALL, 'en_US')
#         str_balance = locale.format_string("%d", self.balance, grouping=True)                             ## Adds deposit value to balance
        
#         self.store_history('debit', amount, comment)

#         print(f'{self.name} your deposit of ₦{amount} was successful your new balance is ₦{str_balance} ')


#     ## TRANSFER
#     def transfer(self, recipient, amount, comment = ''):
        
#         amount = amount.replace(",", "")

#         self.balance -= int(amount)                          ## Remove transfer amount from sender's balance

#         recipient.balance += int(amount)                          ## Add transfer amount from recipient's balance
        
#         locale.setlocale(locale.LC_ALL, 'en_US')
#         str_balance = locale.format_string("%d", self.balance, grouping=True)                             ## Adds deposit value to balance
        

#         self.store_history('debit', amount, comment, recipient.name)

#         print(f'Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful. Your new balance is ₦{str_balance}. ')


#     ## HISTORY
#     def store_history(self, type, amount, comment, receiver = 'same as sender'):
        
#         file = open('Financial_statement.csv', 'a')
#         file.write(f'{type}, {self.name}, {amount}, {comment}, {receiver}\n')

#         print(type, amount, comment, receiver)


# atha = Account('Atha', 23, 'atha_mg@yahoo.com', '08032134387')
# print(atha.account_no)
# atha.deposit("100,000,000")
# atha.withdraw('50,000')

# bolu = Account('Bolu', 23, 'bolu_mg@yahoo.com', '08032134387')
# atha.transfer(bolu, '25,000', 'flexing')



#--------------------------------------------------------------------------------------------------------------------------------------------------

## REFACTORED TO HAVE TRANSACTION USING DEPOSIT AND WITHDRAW METHODS INSTEAD OF WRITING 

import random
import locale

class User:

    def __init__(self, name, age, email, phone):

        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

class Account(User):

   

    def __init__(self, name, age, email, phone):  ## Initialize child class
        super().__init__(name, age, email, phone)  ## Initialize attributes from parent class
        self.balance = 0
        self.account_no = self.generate_acct_no()

    ## METHODS
    def generate_acct_no(self):

        account_num = random.randint(3000000000, 3999999999)
        return str(account_num)

    ## DEPOSIT
    def deposit(self, amount, comment = 'no comment', source = False):

        transaction_label = 'credit'

        if source:
            transaction_type = 'transfer'
            source = source.name
        else:
            transaction_type = 'deposit'
            source = self.name

        amount = amount.replace(",", "")

        self.balance += int(amount)                               ## Adds deposit value to balance

        
        locale.setlocale(locale.LC_ALL, 'en_US')
        str_balance = locale.format_string("%d", self.balance, grouping=True)

        self.store_history(transaction_type, transaction_label, amount, self.name, comment, source)

        print(f'Welldone {self.name} your deposit of ₦{amount} was successful your new balance is ₦{str_balance} ')


    ##WITHDRAW
    def withdraw(self, amount, comment = 'no comment', collector = False):

        transaction_label = 'debit'

        if collector:
            transaction_type = 'transfer'
            collector = collector.name
        else:
            transaction_type = 'withdrawal'
            collector = self.name


        amount = amount.replace(",", "")

        self.balance -= int(amount)                               ## Adds deposit value to balance

        
        locale.setlocale(locale.LC_ALL, 'en_US')
        str_balance = locale.format_string("%d", self.balance, grouping=True)                             ## Adds deposit value to balance
        
        self.store_history( transaction_type, transaction_label, amount, self.name, comment, collector)

        print(f'{self.name} your withdrawal of ₦{amount} was successful your new balance is ₦{str_balance} ')


    ## TRANSFER
    def transfer(self, amount, recipient, comment = ''):

        self.withdraw(amount, comment, recipient)
        recipient.deposit(amount, comment, self)

        amount = amount.replace(",", "")

        self.balance -= int(amount)                               ## Adds deposit value to balance

        
        locale.setlocale(locale.LC_ALL, 'en_US')
        str_balance = locale.format_string("%d", self.balance, grouping=True)  


        print(f'Congrats {self.name} your transfer of ₦{amount} to {recipient.name} was successful. Your new balance is ₦{str_balance}. ')


    ## HISTORY
    def store_history(self, transaction_type, transaction_label, amount, source, comment, receiver = 'same as sender'):
        
        file = open('Financial_statement.csv', 'a')
        file.write(f'{transaction_type}, {transaction_label}, {amount}, {source}, {receiver}, {comment}\n')

        print(transaction_type, amount, comment, receiver)


atha = Account('Atha', 23, 'atha_mg@yahoo.com', '08032134387')
print(atha.account_no)
atha.deposit("100,000,000")
atha.withdraw('50,000')

bolu = Account('Bolu', 23, 'bolu_mg@yahoo.com', '08032134387')
atha.transfer ('25,000', bolu, 'flexing')


