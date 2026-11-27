# print("hello world")
# print("one","two","three")
# print("one","two",sep="-")
# print("hello",end="!")

# a= 5
# b=6
# print(a+b)


# a=int(input("enter first number"))
# b=int(input("enter second number"))
# sum=a + b
# print(sum)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# result = a + b

# print("Addition =", result)



# result=a-b
# print(result)

# multiply=a*b
# print(multiply)
# print("\n")




# age=int(input("Enter your age"))
# height=float(input("height in meters"))
# print(age,height)


#swapping in pythons
# a=5
# b=8

# (a,b)=(b,a)
# print(a,b)


# #reversing in python

# a=6
# b=9
# name=input("Enter your name")
# print(name[::-1])

# messsage=print("""HELLO 
# WELCOME
#  TO PYHTON""")

# if(a%2==0):
#     print("even")
# else:
#     print("odd")


# item1=1
# item2=33
# item3=2
# total=(item1* 2
#         + item2*3
#         +item3*4)

# print("Total",total)


# n=int(input("Enter a number"))
# for i in range(1,11):
#     print(f"{n}*{i})={n*i}")



#ask the user three scores tes1,test2, test3

# test1=int(input("Enter first number"))
# test2=int(input("Enter second number"))
# test3=int(input("Enter third number"))

# #convert each input to float
# test1=float(test1)
# test2=float(test2)
# test3=float(test3)

# #calculate the avarage of three scrores
# avg=(test1+test2+test3)/3
# #store the result in a variable called average
# average=avg
# print("the result is :" + str( average ))



# #combining the Strings
# first="Hello"

# second=", how are you?"
# print(first + second)

# print("1"+"2")

# name="Jonny"
# print(f"Hello {name}")
# pi=3.14
# print(f"{pi:.3f}")

#enter two numbers
# num1=int(input("Enter your first number "))
# num2=int(input("Enter your second number "))

# #calculate both their sum and their product

# sum=num1+num2
# product=num1*num2

# #print the result
# print("sum is ", sum , " and the product is ", product)

# #handle string to number conversion

# print(str(sum)+str(product))

# print(f"{product} {sum}")
# print(f"{product:.5f}")



#  Create a Python script that asks the user for the weight and height and then calculates the Body Mass Index (BMI)
# score. You can try to use F-strings for output

height=float(input("Enter your height in meters"))
weight=int(input("ENter your weight in kg"))

BMI_cal=weight/(height*height)

print(f"{BMI_cal:.4f}")
