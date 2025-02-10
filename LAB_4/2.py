import math
def sq_between(n1, n2):
    if n1 > n2:
        n1 , n2 = n2 , n1
    count = 0
    for i in range(n1,n2+1):
        if (math.isqrt(i))**2 == i : # isqrt -> integeral sqr root a number
            count += 1
    return count

t = int(input("Enter number of testcases "))
if(t>100):
    print("Testcases Exceeded")
    exit
else:
    list1 = []
    print(f"Enter {t} pairs of integers separeted by space")
    for i in range(t):
        N = list(map(int,input().split()))
        list1.append(N)
    for sub_list in list1:
        print(sq_between(sub_list[0],sub_list[1]))