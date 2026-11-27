num1=float(input("Enter first number"))
num2=float(input("Enter Second number"))
operator=input("Enter you operator (-,+,*,/)")

if operator =="-":
    sub=num1-num2
    print(sub)

elif operator=="+":
    add=num1+num2
    print(add)
elif operator=="*":
    mul=num1*num2
    print(mul)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{result:.2f}")
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operator"
   

    


