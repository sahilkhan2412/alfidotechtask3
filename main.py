print("TEMPERATURE CONVERTER")
temp=float(input("Enter temperature : "))
unit=input("Enter unit of measurement (C/F/K): ").upper()
if unit=="C":
    print("Fahrenheit:",(temp * 9/5) + 32)
    print("Kelvin:",temp + 273.15)
elif unit=="F":
    print("Celsius:",(temp - 32 )* 5/9)
    print("Kelvin:",((temp - 32)*5/9)+273.15)
elif unit=="K":
    print("Celsius:",(temp - 273.15)* 5/9)
    print("Fahrenheit:",(temp - 273.15)*5/9)
else:
    print("Invalid unit")