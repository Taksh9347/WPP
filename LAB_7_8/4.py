class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __add__(self,other):
        return self.salary+other.salary
    def __sub__(self,other):
        return self.salary-other.salary
    def __gt__(self,other):
        return self.salary>other.salary
    def __lt__(self,other):
        return self.salary<other.salary
A = Employee('Sam',123.55)
B = Employee('Jhon',234.45)
print(f"Combined salary of {A.name} and {B.name} is {A+B}")
print(f"{A>B}")
print(f"{A<B}")