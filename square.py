# create square with for loop

number = int(input("Input your square's area: "))

for row in range (number): #start from 0, don't need to determine the start number
    for column in range (number):
        print('x ', end='')
    print(' ')