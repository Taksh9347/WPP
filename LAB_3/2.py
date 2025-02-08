n1, n2 = 0, 1
count = 0
list = []
n=30
if n == 1:
   print(n1)
else:
   while count < n:
       list.append(n1)
       sum = n1 + n2
       n1 = n2
       n2 = sum
       count += 1
print(f"First {n} Fibonacci terms")
print(list)
x = int(input("Enter any number "))
if x in list:
   print(f"{x} is FIBO")
else:
   print(f"{x} is not a FIBO")