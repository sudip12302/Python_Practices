# Factorial of a number
n = int(input("Enter a number: "))

# Initialize factorial to 1 and i to 1
factorial = 1 #initialize factorial to 1
i = 1 # Loop from 1 to n and multiply factorial by i

# Loop from 1 to n 
while i <= n:
    factorial = factorial * i #update the value of factorial by multiplying it with i
    i = i + 1 #update the value of i by incrementing it by 1

print("Factorial =", factorial) 