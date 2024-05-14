# number ladder

last = int(input("Input your number: "))

for row in range(1, last+1):
    for column in range(1, row+1):
        print(column, end='')
    print(' ')
    
# let say last = 3
# in first loop
# row = 1, 3+1
# column = 1, 1+1
# it will print 1 as the column will stop at 1 as the end of column is 1+1=2 which will stop at number before 2
# in second loop
# row = 2, 3+1
# column = 1, 2+1
# it will print 12 as the column will stop at 2 as the end of column is 2+1=3 which will stop at number before 3
# in last loop
# row = 1, 3+1
# column = 1, 3+1
# it will print 123 as the column will stop at 3 as the end of column is 3+1=4 which will stop at number before 4

 
