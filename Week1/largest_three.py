# Largest of Three Numbers
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if A >= B and A >= C:
    largest = A
elif B >= A and B >= C:
    largest = B
else:
    largest = C

print("Largest number is:", largest)