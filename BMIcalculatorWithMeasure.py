weight = int(input("What is your weight? (kg): "))
height = int(input("What is your height? (cm): "))


# bmi = weight (kg) / (height * height) (m * m)

# m to cm
height = float(height) / 100

bmi = float(weight) / height ** 2

if bmi < 18.0 :
    result = "You're underweight, contact GP!"
elif bmi >= 18.5 and bmi <= 22.9 :
    result = "You're good, keep doing!"
elif bmi >= 23.0 and bmi <= 24.9 :
    result = "You're overweight, do some excercise!"
elif bmi >= 25.0 and bmi <= 29.9 :
    result = "You might have weight decease 1st stage, contact GP!"
elif bmi >30:
    result = "You're in danger condition, contact GP asap!"
else :
    result = "Cannot measure your BMI, please try agin"


print(f"Your BMI is = " "%.2f" % bmi , f"BMI standard:", result)


'''
<18 below standard
18.5 - 22.9 = good
23.0 - 24.9 = over weight
25.0 - 29.9 = weight decease 1st stage
> 30 = Danger 
'''