sum = 0

while True:
    number = int(input("Input your number: "))
    sum+=number
    print("Total = ", sum)
    if sum>100:
        break 