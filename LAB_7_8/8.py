def decode(code):
    n = len(code)
    ways_to_decode = [0]*(n+1) # create list to store ways to decade strings [0,0,0....n+1 times]
    ways_to_decode[0] = 1
    if(n==0 or code[0]=='0'):
        return 0
    else:
        ways_to_decode[1]=1
        for i in range(2,n+1):
            one_digit = int(code[i-1])
            two_digit = one_digit + 10*int(code[i-2])
            if(one_digit>=1):
                ways_to_decode[i] += ways_to_decode[i-1]
            if(two_digit>=10 and two_digit<=26):
                ways_to_decode[i] += ways_to_decode[i-2] 
    return ways_to_decode[n]
str = input("Enter encoded message : ")
print(decode(str))
