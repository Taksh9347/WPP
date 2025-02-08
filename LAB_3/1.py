def digital_root(n):
    sum = 0
    while(n>0):
        sum = sum + n%10
        n = n//10
    if(sum<=9):
        return sum
    return digital_root(sum)
n = int(input("Enter a number "))
print(digital_root(n))