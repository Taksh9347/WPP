class BankAccount:
    def __init__(self,acc_no,balance=0.0):
        self.acc_no = acc_no
        self.balance = balance
    def deposit(self):
        d_amount = float(input("Enter deposit amount : "))
        if d_amount>0:
            self.balance += d_amount
            print(f"Successfully deposited {d_amount} ")
        else:
            print("Amount cant be negative")
    def withdraw(self):
        w_amount = float(input("Enter withdraw amount : "))
        if 0<w_amount<=self.balance:
             self.balance -= w_amount
             print(f"Successfully withdraw {w_amount} ")
        elif 0>w_amount:
            print("Amount cant be neagtive ")
        else:
            print("Amount cant exceed current balance ")
    def show_details(self):
        print(f'''ACCOUNT NUMBER : {self.acc_no}\nBALANCE : {self.balance} ''')

A = BankAccount('A2345')
print('''1) Show Details
2) Deposit
3) Withdraw
4) Exit''')
while(1):
    choice = int(input("Enter Choice : "))
    if(choice==1):
        A.show_details()
    elif(choice==2):
        A.deposit()
    elif(choice==3):
        A.withdraw()
    elif(choice==4):
        print("EXITING...")
        exit(0)
    else:
        print("Invalid Choice")