# guess the random dice number
# 1, 2, 3, 4, 5, 6

import random



myrandom = random.randrange(1,7) # 1-6
loop = 1
correct = False

print("You've only 3 chances \n")

while True:
    guessNumber = int(input("Input your guess number (1-6): "))

    correct = (guessNumber == myrandom)
    if not correct :
        if(guessNumber > myrandom):
            print("Just so close, less than")
        if(guessNumber < myrandom):
            print("Just so close, more than")
    if correct:
        print("Wow!!! you're so lucky, the dice number is: ", myrandom)
        break
    if guessNumber < 0 or loop == 3:
        break
    loop += 1

if not correct:
    print("Ahhh!!! it's not your day")
    print("The dice number is: ", myrandom)