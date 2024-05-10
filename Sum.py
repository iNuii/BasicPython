# sum the number with loop while

loop = int(input("Determine the summation loop: "))
i=1 # counter

summation = 0 # sum the number for the loops
avg = 0

while i<=loop:
    summation+=i # store the sum of i on each loop
    print("Sum in ", i, "loops = ", summation)
    i+=1

avg = summation/loop

print("Summation = ", summation)
print("Average of sum number = ", avg)