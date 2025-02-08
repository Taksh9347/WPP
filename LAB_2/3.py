def divisors(n):
    x=n
    arr = []
    while (n!=0):
        arr.append(n%10)
        n=n//10

    count=0
    for i in arr:
        if(x%i == 0):
            count+=1
    return count 

t = int(input("Enter number of testcases\n"))
if(t>15):
    print("Testcases Exceeded")
else:
    n = list(map(int,input(f"Enter {t} numbers separated by space\n").split()))
    for num in n:
        print(divisors(num))