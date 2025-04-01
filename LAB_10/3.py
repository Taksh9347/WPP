# (x,y) -> (r,theta)
import random
import numpy as np
N = int(input("Enter a number "))
if N>=10:
    points = [(random.randint(-10,10),random.randint(-10,10)) for _ in range(N)]
    point_arr = np.array(points)
    print(f"{N} random points bw -10 to 10 are ")
    print(point_arr)
    x = point_arr[:,0] # get all x coordinates (i.e, elements of first column)
    y = point_arr[:,1]
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y,x)  # arctan gives only tan-1(y/x) but arctan2 checks every quadrant
    res = np.column_stack([r,theta])
    print(res)
else:
    print("Enter N>=10")