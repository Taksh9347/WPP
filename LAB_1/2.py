import random
arr1 = [random.randint(0,1) for i in range(100)]
print(arr1)
arr2 = []
count=0
max_occurence=0
for i in arr1:
    if(i==0):
        count+=1
    else:
        max_occurence = count
        if(max_occurence!=0):
            arr2.append(max_occurence)
        count = 0
print(f"longest run of zeros is {max(arr2)}")