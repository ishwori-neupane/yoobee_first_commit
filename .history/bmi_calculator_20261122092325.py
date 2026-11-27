
# BMI Calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

BMI_cal = weight / (height ** 2)

print(f"Your BMI is: {BMI_cal:.4f}")

if height <= 0:
    print("Your height must be greater than 0.")

elif weight <= 0:
    print("Your weight must be greater than 0.")

else:
    BMI_cal = weight / (height ** 2)

    print(f"Your BMI is: {BMI_cal:.4f}")
