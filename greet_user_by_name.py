
# Ask the user to enter their full name
full_name = input("Enter your name: ")

# Find the position of the space
space = full_name.find(" ")

# Extract first and last names
first_name = full_name[0:space]
last_name = full_name[space+1:]

# Capitalize both names
first_name = first_name.capitalize()
last_name = last_name.capitalize()

# Display the result
print(f"Your first name is {first_name}")
print(f"Your last name is {last_name}")
print(f"Welcome, {first_name} {last_name}!")
