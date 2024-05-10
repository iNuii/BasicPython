# Multiplication table

first = int(input("Input first multiply group: "))
last = int(input("Input last multiply group: "))


for x in range (first,last+1):
    print("Multiply group of = ", x )
    for y in range (1,13):
        print(x, "x", y ," = ", (x*y))