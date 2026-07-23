
# Check if a number is odd or even
# Prompt user to enter a number and convert it to integer
number = int(input("Enter a number: "))

# Check if the number is even using modulo operator (%)
# If number % 2 equals 0, the number is even
if number % 2 == 0:
    print("Number is Even")
else:
    # If the remainder is not 0, the number is odd
    print("Number is Odd")
    