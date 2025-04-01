import numpy as np
import matplotlib.pyplot as plt
import random
f = lambda x: x**3 - x - 4

def randomprobe(f):
    while True:
        a,b = random.uniform(-10,10),random.uniform(-10,10)
        if a>b :
            a,b = b,a
        if f(a)*f(b) < 0:
            return a,b
        
def bisection(f,a,b,iterations=100,tol=1e-6,):
    updates = []
    for _ in range(iterations):
        c = (a+b)/2
        updates.append(c)
        if abs(f(c)) < tol:
            break
        elif f(c)*f(b) < 0: # root lies in [c,b]
            a = c
        else:
            b = c
    return np.array(updates)

def Plot(f,update):
    x_vals = np.linspace(-3, 3, 1000)
    y_vals = f(x_vals)
    plt.figure(figsize=(7,7))
    plt.plot(x_vals, y_vals, label="f(x) = x**3 - x - 4", color="green")
    plt.scatter(update,f(update),color="red",label="steps")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")  
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.xlabel("x ---->")
    plt.ylabel("f(x) ---->")
    plt.title("Graph of f(x) = x**3 - x - 4")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    a,b = randomprobe(f)  
    update = bisection(f,a,b,1000)
    Plot(f,update)  