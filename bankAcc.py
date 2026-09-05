class Bank:
    def __init__(self,acc_name,acc_num,balance):
        self.acc_name=acc_name
        self.acc_num=acc_num
        self.balance=balance

    def deposit(self,money):
        self.balance+=money
        print("Your money has been deposit in your account and your current balance is: ",self.balance)
    def diplay(self):
        print("Account Name: ",self.acc_name)
        print("Account Number: ",self.acc_num)
        print("Balance: ",self.balance)

a1=Bank("Alyan",1234567,10000)
a1.diplay()
a1.deposit(5000)
a1.diplay()