import math
class Vector_2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    def angle(self):
        return math.atan2(self.y,self.x)
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    def dot_prod(self,other):
        return self.x*other.x + self.y*other.y
    def cross_prod(self,other):
        return f"{self.x*other.y - self.y*other.x}k"
    def display(self):
        print(f"({self.x},{self.y})")
class Vector_3D(Vector_2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def angle(self):
        return math.atan2(self.y,self.x)
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)
    def dot_prod(self,other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def cross_prod(self,other):
        return Vector_3D(self.y*other.z - self.z*other.y,self.x*other.z-self.z*other.x,self.x*other.y-self.y*other.z)
    def display(self):
        print(f"({self.x},{self.y},{self.z})")

A = Vector_3D(1,2,3)
B = Vector_3D(1,1,1)
A.cross_prod(B).display()

C = Vector_2D(1,2)
D = Vector_2D(3,4)
print(C.cross_prod(D))