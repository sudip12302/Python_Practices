
# Find the GCD of two numbers using Euclidean algorithm
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean algorithm to find GCD
#if b is not zero, then we can continue to find GCD
while b != 0:
    temp = b #store the value of b in temp variable
    b = a % b #update the value of b to the remainder of a divided by b
    a = temp #update the value of a to the value of temp

print("GCD is:", a)