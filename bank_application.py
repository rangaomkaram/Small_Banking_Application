#simple bank application system
import sys
class Customer:
    """ Customer class with bank related operations"""
    bankname = "Indian Ranga Bank"
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
        print("After deposit the balance:",self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Funds in your account so we can't perform thsi operation")
            sys.exit()
        self.balance=self.balance-amt
        print("After withdraw the remaining balance:",self.balance)
print("Heartly Weclome to",Customer.bankname)
Customername=input("Enter the name of customer:")
c=Customer(Customername)
while True:
    print("d-Deposit\nw-WIthdraw\ne-Exit")
    option=input("Choose your option:")
    if option=='d' or option=='D':
        amt=float(input("Enter the amount to deposit :"))
        c.deposit(amt)

    elif option=='w'or option=='W':
        amt=float(input("Enter the amount to withdraw :"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for Banking\nVisit again")
        sys.exit()

    else:
        print("Choose valid option")

