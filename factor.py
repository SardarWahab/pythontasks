# Program to calculate the factorial of a number

# Get input from the user
number = int(input("Enter a number: "))

# Initialize the factorial variable
factorial = 1

# Calculate the factorial using a loop
for i in range(1, number + 1):
    factorial *= i

# Print the result
print(f"The factorial of {number} is {factorial}")
