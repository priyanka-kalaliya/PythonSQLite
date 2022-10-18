import sys
import sqlite3
import os

class Bank:


    def __init__(self):
        if os.path.exists('demo.db'):
            self.conn=sqlite3.connect('demo.db')
            self.c=self.conn.cursor()
            self.c.execute('SELECT * FROM record')
            emp2=self.c.fetchall()

        else:
            pass


    def name(self):
        print("Enter your Name : ")
        conn=sqlite3.connect('demo.db')
        c=conn.cursor()
        d=c.execute('SELECT name FROM bank')


    def screen_options(self):
        print('1.  Deposit')
        print('1.  Withdraw')
        print('1.  Check Balance')
        print('1.  Exit')


        c=int(input('Enter Choice : '))
        return c

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))          
        d=c.execute('SELECT balance FROM bank')
        d += amount
        c.execute('update bank set balance=d')
        print("\n Amount Deposited:", amount)




    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")




    def check_balance(self):
        amount = float(input("Total Balance: "))
        self.balance = amount
        print("\n Total Balance:", amount)




    def exit(self):
        pass

b1=Bank()

while True:
    k=b1.screen_options()
    if k==1:
        b1.deposit()
    elif k==2:
        b1.withdraw()
    elif k==3:
        b1.check_balance()
    elif k==4:
        sys.exit('Thankyou for visiting our Bank')

    else:
        print('Input valid Number..')











conn.close()