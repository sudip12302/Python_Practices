#take a input from user and find the sum of all numbers from 1 to n
n = int(input("Enter a number: "))   # Ask the user to enter a number and convert it to an integer
sum = 0                              # Initialize a variable sum to store the sum of numbers
for i in range(1, n+1):              # Loop from 1 to n (inclusive)
    sum = sum + i                    # Add the current number i to the sum
print("The sum of all numbers from 1 to", n, "is:", sum)  # Print the final sum