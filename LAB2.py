# 1
# str = (input("Enter any string "))
# str2 = ''
# extra = ''
# i=1
# for ch in str:
#     extra = extra + ch
#     i=i+1
#     if(i%2==0):
#         str2 = str2 + extra + " "
#         extra = ''
# res = str2.title()
# str2=''
# for ch in res:
#     if(ch!=' '):
#         str2 = str2 + ch
# str4 = str2[0].lower() + str2[1:]
# if(len(str4)!=len(str)):
#     str4 = str4 + str[len(str)-1].capitalize()
# print(str4)

# 2
# def is_valid_price(price):
#     if price.count('.') > 1:  # float value cant hv more than one decimal points
#         return False
#     else :
#         return True

# dict = {}
# while True:
#     product = input("Enter the product name (or 'q' to quit): ").strip()
#     if product.lower() == 'q':
#         break
#     if product in dict:
#         print(f"Product '{product}' already exists with a price of {dict[product]}.")
#     else:
#         while True:
#             price = input(f"Enter the price for '{product}': ").strip()
#             if is_valid_price(price):
#                 price = float(price) 
#                 dict[product] = price
#                 break   
#             else:
#                 print("Invalid price")
# while True:
#     find_prod = input("\nEnter Product name to check its price (or 'q' to quit): ").strip()
#     if find_prod.lower() == 'q':
#         print("END")
#         break
#     if find_prod in dict:
#         print(f"Price of {find_prod} = {dict[find_prod]}.")
#     else:
#         print(f"'{find_prod}' is not in the dictionary.")

# 3
# #1<=testcase<=15
# #0<=N<=pow(10,10)
# def divisors(n):
#     x=n
#     arr = []
#     while (n!=0):
#         arr.append(n%10)
#         n=n//10

#     count=0
#     for i in arr:
#         if(x%i == 0):
#             count+=1
#     return count 

# t = int(input("Enter number of testcases\n"))
# if(t>15):
#     print("Testcases Exceeded")
# else:
#     n = list(map(int,input(f"Enter {t} numbers separated by space\n").split()))
#     for num in n:
#         print(divisors(num))