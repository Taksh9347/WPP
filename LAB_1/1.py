list_A=[]
list_B=[]
for i in range(50):
    list_A.append(i)
    if(i*i<=50 and i!=0):
        list_B.append(i*i)
print("Integers form 0 to 49")
print(list_A)
print()
print("Squares within 1 to 50")
print(list_B)
print()

list_C=[]
x = ""
for i in range(1,27):
    x = (i*chr(i+96))
    list_C.append(x)
print("Alaphabets")
print(list_C)
print()