#1 n=45893 ->> 2
# def digital_root(n):
#     sum = 0
#     while(n>0):
#         sum = sum + n%10
#         n = n//10
#     if(sum<=9):
#         return sum
#     return digital_root(sum)
# n = int(input("Enter a number "))
# print(digital_root(n))

#2 ISfibo
n = 20
n1, n2 = 0, 1
count = 0
list = []
if n <= 0:
   print('invalid')
elif n == 1:
   print(n1)
else:
   while count < n:
       list.append(n1)
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1
print(list)
x = int(input("Enter any number "))
if x in list:
   print("Yes")
else:
   print("no")