weight = int(input("What is your weight? (kg): "))
height = int(input("What is your height? (cm): "))


# bmi = weight (kg) / (height * height) (m * m)

# m to cm
height = float(height) / 100

bmi = float(weight) / height ** 2

print(f"Your BMI is {bmi}")
