# summation with average
start, stop = 1,5
sum = 0
avg = 0

while start<=stop:
    number = int(input("input the number: "))
    sum+=number # sum number from the input
    start+=1
    
avg = sum/stop
print("Summation of all numbers is: ", sum)
print("Average of all numbers is: ", avg)
    