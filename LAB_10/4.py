import numpy as np
arr = np.array([[8,4,5],
               [3,14,6]])
l1 ,l2 ,l3 =[],[],[]
for i in arr.flat:
    l1.append(str(i).ljust(15,"_"))
    l2.append(str(i).rjust(15,"_"))
    l3.append(str(i).center(15,"_"))
arr = np.array(([l1],[l2],[l3]))
print(arr)