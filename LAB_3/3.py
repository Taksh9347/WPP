def height(n):
    height = 1
    for i in range(n):
        if(i%2!=0):
            height += 1
        else:
            height *= 2
    return height

t = int(input("Enter number of testcases "))
if(t>10):
    print("Testcases Exceeded")
    exit
else:
    print(f"Enter {t} numbers")
    N = list(int(input("")) for i in range(t))
    for num in N:
        print(height(num))