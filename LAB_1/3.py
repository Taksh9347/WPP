def convert_length(feet, choice):
    units = [feet * 12,feet / 3,feet / 5280,feet * 304.8,feet * 30.48,feet * 0.3048,feet * 0.0003048]
    return units[choice - 1]

feet = float(input("Enter length in feet "))
print("\nConversion options")
print("1.Inch")
print("2.Yard")
print("3.Mile")
print("4.Millimeter")
print("5.Centimeter")
print("6.Meter")
print("7.Kilometer")
options=["inch","Yard","Mile","Millimeter","Centimeter","Meter","Kilometer"]

x = int(input("\nEnter option "))
if(1<=x<=7):
    print(f"{feet} feet = {convert_length(feet,x)} {options[x-1]}")
else:
    print("Invalid Option!!\n")