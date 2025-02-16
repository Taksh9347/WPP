import random
class Rock_Paper_Scissor:
    def __init__(self):
        self.choices = ['rock','paper','scissor']
        self.u = 0
        self.c = 0
    def User_choice(self):
        while True:
            user = input("Enter user choice : ").lower()
            if user in self.choices:
                self.user = user
                break
            else:
                print("Invalid Choice")
    def Comp_choice(self):
        self.comp = random.choice(self.choices)
        print("Computer","=",self.comp)
    def Winner(self):
        if(self.user==self.comp):
            print("Tie")
        elif(self.user=='rock' and self.comp=='scissor'):
            self.u+=1
        elif(self.user=='scissor' and self.comp=='paper'):
            self.u+=1
        elif(self.user=='paper' and self.comp=='rock'):
            self.u+=1
        else:
            self.c+=1
    def Start_Game(self):
        n = int(input("Enter Number of rounds : "))
        print()
        for i in range(n):
            print(f"Round{i+1}")
            self.User_choice()
            self.Comp_choice()
            self.Winner()
            self.Display_score()
    def Display_score(self):
        print(f"User = {self.u} and Comp = {self.c}\n")
    def Result(self):
        if(self.u>self.c):
            print("USER WON")
        elif(self.u==self.c):
            print("Tie")
        else:
            print("COMPUTER WON")

A = Rock_Paper_Scissor()
A.Start_Game()
A.Result()