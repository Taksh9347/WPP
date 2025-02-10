t = int(input("Enter number of testcases "))
if t>=10 and t<=0:
    print("Testcase Exceeded ")
    exit
else:
    N = list(input("") for i in range(t))
    for str in N:
        str = str.lower()
        n = len(str)
        count = 0
        for i in range(0,n//2,1): # we dont hv to consider middle element if len(str) is odd
            count += abs(ord(str[i]) - ord(str[n-1-i]))
        print(count)