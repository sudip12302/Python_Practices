#take a input from user and find the greatest among two numbers
a = float(input("Enter first number: "))   # Ask the user to enter the first number and convert it to an integer
b = float(input("Enter second number: "))  # Ask the user to enter the second
if a > b:                               # Check if the first number is greater than the second number
    print("The greatest number is:", a)  # If true, print the first number as the greatest
else:
    print("The greatest number is:", b)  # If false, print the second number as the greatest