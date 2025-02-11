t = int(input("Enter number of testcases "))
s = list(input("") for i in range(t))
print("Output")
for j in range(t):
    arr = list(ord(_) for _ in s[j])
    n = len(arr)
    x=0
    for i in range(0,n,1):
        if(x==0):
            if(arr[n-i-1]>arr[n-i-2]):
                arr[n-i-1],arr[n-i-2] = arr[n-i-2],arr[n-i-1]
                x+=1
            elif(arr[n-i-1]<=arr[n-i-2]):
                pass
    s1 = ""
    for i in range(n):
        s1 = "".join([s1,chr(arr[i])])
    if(s[j]==s1):
        print("No answer")
    else:
        print(s1)