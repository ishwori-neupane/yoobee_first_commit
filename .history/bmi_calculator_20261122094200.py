
# BMI Calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

BMI_cal = weight / (height ** 2)

print(f"Your BMI is: {BMI_cal:.4f}")


if BMI_cal<18.5:
    print("You have an uderweight")
elif BMI_cal > 18.5  | BMI_cal<24.9:
    print("Your weight is normal")
elif BMI_cal > 25 | BMI_cal 29.9:
    print(" You have an overwigth.... start to diet hahhah")
elif BMI_cal >29.0:
    print(" You have an overwigth.... start to diet hahhah")
else:
    print("Check your BMI index timely")











if height <= 0:
    print("Your height must be greater than 0.")

elif weight <= 0:
    print("Your weight must be greater than 0.")

else:
    BMI_cal = weight / (height ** 2)

    print(f"Your BMI is: {BMI_cal:.4f}")
