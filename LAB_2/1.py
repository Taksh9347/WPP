str = (input("Enter any string "))
str2 = ''
extra = ''
i=1
for ch in str:
    extra = extra + ch
    i=i+1
    if(i%2==0):
        str2 = str2 + extra + " "
        extra = ''
res = str2.title()
str2=''
for ch in res:
    if(ch!=' '):
        str2 = str2 + ch
str4 = str2[0].lower() + str2[1:]
if(len(str4)!=len(str)):
    str4 = str4 + str[len(str)-1].capitalize()
print(str4)