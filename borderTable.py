# create table border with for loop

number = int(input("Input your table's size: "))

for row in range (number): #start from 0, don't need to determine the start number
    for column in range (number):
        if row == 0 or row == number-1 or column == 0 or column == number-1:
            print('X ', end='')
        else:
            print("  ", end='')
    print(' ')