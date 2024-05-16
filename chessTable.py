number = int(input("Input your square's area: "))

for row in range (number): #start from 0, no need to determine the start number
    for column in range (number):
        print('X ', end='') if (row + column) % 2 == 0 else print('0 ', end='')
    
    print(' ')
    


"""
how it calculate:
3 * 3 

first loop:
row 0 + column 0 % 2 = 0
row 0 + column 1 % 2 = 1
row 0 + column 2 % 2 = 0

second loop:
row 1 + column 0 % 2 = 1
row 1 + column 1 % 2 = 0
row 1 + column 2 % 2 = 1

...

display 
first loop:  X0X
second loop: 0X0


"""