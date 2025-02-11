t = int(input("Enter number of testcase "))
if(t>=1 and t<=10):
    N = list(map(int,input(f"Enter {t} numbers separated by space\n").split()))
    for num in N:
        if(num%2==0):
            print(int((num/2)**2))
        else:
            x=num//2
            print(int((x)*(x+1)))
else:
    print("ERROR! Out of constraints")