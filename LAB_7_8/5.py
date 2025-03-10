from abc import ABC, abstractmethod
import math
class SHAPE(ABC):
    @abstractmethod
    def Area(self):
        pass
    @abstractmethod
    def Perimeter(self):
        pass
class Circle(SHAPE):
    def __init__(self,r):
        self.r = r
    def Area(self):
        return math.pi*self.r**2
    def Perimeter(self):
        return 2*math.pi*self.r
class Rectangle(SHAPE):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def Area(self):
        return self.l*self.b
    def Perimeter(self):
        return 2*(self.l+self.b)
    
A ,B = Circle(10) ,Rectangle(20,10)
print(f"Area of circle = {A.Area()} \nPerimeter of circle = {A.Perimeter()}\n")
print(f"Area of Rectangle = {B.Area()}\nPerimeter of rectangle = {B.Perimeter()}\n")