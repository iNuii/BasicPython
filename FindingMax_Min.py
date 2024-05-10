# find max / min

max, min = 0,9999

while True:
    number = int(input("Input your number: "))
    if number < 0:
        break
    if number > max:
        max = number
        
    if number < min:
        min = number
        
print ("Max number input is: ", max)
print ("Min number input is: ", min)