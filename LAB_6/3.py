class converter:
    def __init__(self,l,unit):
        self.l = l
        self.unit = unit
        self.units = {'inches':l*0.0254,'feet':l*0.3048,'yards':l*0.9144,'kilometer':l*1000,'meter':l*1,'centimeter':l*0.01,'millimeter':l*0.001}
    def length_to_meter(self):
        self.l = self.units[self.unit]
        self.unit = 'meter'
        return self.l
    def Print(self):
        print(f"{self.l} {self.unit}")
    def feet(self):
        print(f"{self.l*3.28} feet")
    def inches(self):
        print(f"{self.l*39.37} inches")
    def yards(self):
        print(f"{self.l*1.0936} yards")
    def kilometer(self):
        print(f"{self.l*0.001} kilometer")
    def meter(self):
        print(f"{self.l*1} meter")
    def centimeter(self):
        print(f"{self.l*100} centimeter")
    def millimeter(self):
        print(f"{self.l*1000} millimeter")
    def miles(self):
        print(f"{self.l*0.00062137} miles")
    
A = converter(9.2,'inches')
A.Print()
A.length_to_meter()
A.feet()
A.kilometer()
A.miles()