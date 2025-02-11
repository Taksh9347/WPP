print("Enter two numbers")
l,r = int(input()),int(input())
if(l<=r<=1000):
    arr = []
    for i in range(l,r+1,1):
        for j in range(i,r+1,1):
            arr.append(i^j)
    print(f"maximum xor value = {max(arr)}")
else:
    print("ERROR! Out of constraints")