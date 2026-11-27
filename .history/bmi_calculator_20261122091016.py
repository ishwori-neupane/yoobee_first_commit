
#  Create a Python script that asks the user for the weight and height and then calculates the Body Mass Index (BMI)
# score. You can try to use F-strings for output

height=float(input("Enter your height in meters"))
weight=int(input("Enter your weight in kg"))

BMI_cal=weight/(height**2)

print(f"{BMI_cal:.4f}")


