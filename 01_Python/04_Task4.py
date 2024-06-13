def Get_Area(radius):
    Area = 3.14*(radius)**2
    return Area

input = float(input("Enter circle radius: "))
Area = Get_Area(input)
print(f"Area = {Area}")