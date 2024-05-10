# change F degree to C degree
# F = (C*9/5)+32
# change C degree to F degree
# C = (F-32)*5/9
temp = input("input the temperature (C/F): ")

# string operator
degree = int(temp[:-1])
unit = temp[-1:].upper()


if unit == "C":
    # change to F
    tempResult = (9*degree)/5+32
    unitResult = "F"
if unit == "F":
    # change to C
    tempResult = (degree-32)*5/9
    unitResult = "C"
    

print(f"Change from temperature", degree, unit, "to", "unitResult",  f"The temperature is ", tempResult, unitResult)






