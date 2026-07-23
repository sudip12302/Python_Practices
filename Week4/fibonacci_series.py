# Program to print the Fibonacci series up to a given n number given by the user using lists
n= int(input("Enter a number: "))   # Ask the user to enter a number and convert it to an integer
a= [1,1]  # Initialize a list with the first two numbers of the Fibonacci series
for i in range(2,n):  # Loop from 2 to n (exclusive) to generate the Fibonacci series
    next = a[i-1] + a[i-2]  # Calculate the next number in the series by adding the last two numbers
    a.append(next)  # Add the next number to the list
print("The Fibonacci series up to", n, "is:", a)  # Print the Fibonacci series