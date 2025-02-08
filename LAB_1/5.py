names=[]
print("Enter 4 student names")
for i in range(4):
    print("Student",i+1)
    x = input()
    if(len(x)<=15):
       names.append(x)
    else:
        print("Error! Student name length exceeded","(Enter name under 15 characters)")
        x = input()
        names.append(x)
x = ""
rev = ""
for i in range(len(names)):
    x = names[i]
    rev = x[::-1]
    names[i]=rev
print("\nNames of Students")
print(names)