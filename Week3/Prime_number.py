# Program to check whether a number is prime or not

n = int(input("Enter a number: "))   # Ask the user to enter a number and convert it to an integer

i = 2                                # Start checking divisibility from 2

while i < n:                         # Loop runs while i is less than n
    if n % i == 0:                   # Check if n is divisible by i (remainder is 0)
        print("Not Prime Number")    # If divisible, the number is not prime
        break                        # Stop the loop because we already know it is not prime
    i = i + 1                        # Increase i by 1 to check the next number

if i == n:                           # If the loop finishes and i becomes equal to n
    print("Prime Number")            # It means no number divided n, so it is prime9
 


  

