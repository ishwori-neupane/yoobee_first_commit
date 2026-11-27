
# BMI Calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

if height <= 0 or weight <= 0:
    print("Height and weight must be greater than zero.")

else:
    BMI_cal = weight / (height ** 2)

    print(f"Your BMI is: {BMI_cal:.4f}")

    if BMI_cal < 18.5:
        print("You are underweight.")

    elif BMI_cal < 25:
        print("Your weight is normal.")

    elif BMI_cal < 30:
        print("You are overweight.")

    else:
        print("You are obese, you need to start dieting hehe.")











if height <= 0:
    print("Your height must be greater than 0.")

elif weight <= 0:
    print("Your weight must be greater than 0.")

else:
    BMI_cal = weight / (height ** 2)

    print(f"Your BMI is: {BMI_cal:.4f}")
