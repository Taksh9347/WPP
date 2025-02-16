import random
import string
class Pass_Manager:
    def __init__(self):
        self.old_pass = [''.join(random.choices(string.ascii_letters+string.digits,k=5)) for i in range(10)]
        self.curr_pass = self.old_pass[-1]
    def get_pass(self):
        print(f"curr_pass = {self.curr_pass}\nList of old passwords : {self.old_pass}")
    def set_pass(self,new_pass):
        if new_pass in self.old_pass:
            print("New pass is same as past passwords.")
        else:
            self.old_pass.append(new_pass)
            self.curr_pass = self.old_pass[-1]
            print("Successfully changed your password")
    def is_correct(self, str_ing):
        return str_ing == self.curr_pass
    
A = Pass_Manager()
print('''1) Get current password and list of old passwords
2) Set a new password
3) Check current password 
4) Exit''')
while(1):
    choice = int(input("Enter Choice : "))
    if(choice==1):
        A.get_pass()
    elif(choice==2):
        new = input("Enter new password : ")
        A.set_pass(new)
    elif(choice==3):
        s = input("Enter string : ")
        print(A.is_correct(s))
    elif(choice==4):
        print("EXITING...")
        exit(0)
    else:
        print("Invalid Choice")