class Banksystem():
    def __init__(self):
        self.balance = 0000000000000000000000

    def deposite(self):
        confirm_deposite = input(" Do you wants to deposite? yes/no \n")
        if confirm_deposite =='yes':
            deposite_amount = eval(input("How much do you want to deposite? \n"))
            self.balance += deposite_amount
            print("Deposite was successful. New amount is {}".format(self.balance))
        elif confirm_deposite == "no":
            print("Thank you for your time!!!")            

    def withdraw(self):
        confirm_withdraw = input("Do you want to withdraw? yes/no \n")
        if confirm_withdraw =='yes':
            withdraw_amount = eval(input('How much do you want to withdraw?\n'))
            if withdraw_amount > self.balance:
                overdraft = input('You do not have sufficient balance to complete this transaction.\n would you like to request an overdraft? yes/no \n ')
                if overdraft == 'yes':
                    print('You request is being review and an email will be send soon')
          

            else:
                self.balance-= withdraw_amount
                print(" You have successful withdraw.New amount is {}".format(self.balance))
        if confirm_withdraw == 'no':
            print("Thank you for your time!!!")                 

bank =Banksystem()
bank.deposite()        
bank.withdraw()        