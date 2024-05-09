


money = int(input("Input your to exchange: "))

if money >= 1000 :
    print("1000 baht = " , money//1000 , "bank notes")
    money %= 1000
    
if money >= 500 :
    print("500 baht = ", money//500 , "bank notes")
    money %= 500
    
if money >= 100 :
    print("100 baht = ", money//100 , "bank notes")
    money %= 100
    
if money >= 50 :
    print("50 baht = ", money//50 , "bank notes")
    money %= 50
    
if money >= 20 :
    print("20 baht = ", money//20 , "bank notes")
    money %= 20