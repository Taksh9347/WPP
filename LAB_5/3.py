def lexico(w):
    arr = list(w)
    n = len(arr)
    i = n-2 # start from second last element
    while (i>=0 and arr[i]>=arr[i+1]):   # eg. dkhc d<k so here i = 0
        i-=1
    if(i==-1):
        return "no answer"
    else:
        j=n-1 # start from last element
        while(j>=i and arr[j]<=arr[i]): # check for larger char afte index 'i' , h>d so j=2
            j-=1

        arr[i],arr[j]=arr[j],arr[i] # swapping to get "hkdc", but it should be "hkcd" to be next lexicographical string
        s = "".join(arr)

        return s[:i+1] + s[i+1:][::-1]# reversing the rest of string to get next smallest string
t = int(input("Enter number of testcases "))
list1 = list(input("") for i in range(t))
for w in list1:
    print(lexico(w))