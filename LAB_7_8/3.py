class Bank:
    def __init__(self):
        self.accounts = {'AccNo.':['Name1',150.00],'B123':['Name2',250.00]}

    def Create_acc(self,amt=0.0):
        name = input("Enter name : ")
        self.name = name
        self.amt = amt
        while(True):
            acc_num = input("Enter account number : ")
            if acc_num.isalnum():
                if acc_num in self.accounts:
                    print("!! ACCOUNT ALREADY IN USE !! \nEnter Valid Account number")
                else:
                    self.accounts.update({acc_num:[name,amt]})
                    break
    def Deposit(self):
        s = input("Enter account number in which you want to deposit : ")
        if s in self.accounts:
            d_amt = float(input("Enter deposit amount : "))
            self.accounts[s][1] += d_amt
            print(f"Successfully deposited {d_amt} \nNew Balance = {self.accounts[s][1]}")
        else:
            print("Account does not exist")
    def Withdraw(self):
        x = input("Enter account number in which you want to deposit : ")
        if x in self.accounts:
            w_amt = float(input("Enter wihtdrawal amount : "))
            if(w_amt>self.accounts[x][1]):
                print("Withdrawal amt cant exceed current balance ")
            else:
                self.accounts[x][1] -= w_amt
                print(f"Withdrawal Successfull \nNew Balance = {self.accounts[x][1]}")
        else:
            print("Account does not exist")
    def Transfer(self):
        s1 = input("Enter 'FROM' account number :")
        s2 = input("Enter 'TO' account number :")
        if s1 and s2 in self.accounts:
            t_amt = float(input("Enter transfer amount : "))
            if(t_amt>self.accounts[s1][1]):
                print("Transfer amount cant exceed current balance ")
            else:
                self.accounts[s1][1] -= t_amt
                self.accounts[s2][1] += t_amt
                print(f"Successfully transfered {t_amt}\nNew Balance of TO account is {self.accounts[s2][1]}")
    def show_all_acc(self):
        print(self.accounts)

A = Bank()
print('''1) Create Account
2) Deposit
3) Withdraw
4) Transfer
5) Show all accounts 
6) Exit''')
while(1):
    choice = int(input("Enter Choice : "))
    if(choice==1):
        A.Create_acc()
    elif(choice==2):
        A.Deposit()
    elif(choice==3):
        A.Withdraw()
    elif(choice==4):
        A.Transfer()
    elif(choice==5):
        A.show_all_acc()
    elif(choice==6):
        print("EXITING...")
        exit(0)
    else:
        print("Invalid Choice")