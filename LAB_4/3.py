# ord(a) = 97 ord(z) = 122
s = input("Enter any string ")
# s = "THE QUICK BROWN FOX jumps Over THE lazy Dog"
s = s.lower()
s = s.replace(" ","")
list1 = [] # for storing ascii values of each alphabet
for char in s:
    list1.append(ord(char))
list2 = [] # for removing multiple occurences of ascii values
for num in list1:
    if num not in list2:
        list2.append(num)
list2.sort()
LIST = [i for i in range(97,123)] # ascii values from a to z
if(LIST == list2):
    print("Panagram")
else:
    print("Not a Panagram")