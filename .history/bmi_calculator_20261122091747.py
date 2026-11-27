
#  Create a Python script that asks the user for the weight and height and then calculates the Body Mass Index (BMI)
# score. You can try to use F-strings for output

height=float(input("Enter your height in meters"))
weight=float(input("Enter your weight in kg"))

if height <=0:
    print("your height must be greater then 0")
if weight <=0 :
    print("Your weight must be greter then 0")

BMI_cal=weight/(height**2)

print(f"{BMI_cal:.4f}")


