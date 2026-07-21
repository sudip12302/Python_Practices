
# Find the largest number among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

#check if a is greater than b and c
if a > b and a > c:
    largest = a
    #check if b is greater than a and c
elif b > a and b > c:
    largest = b
    #if a and b are not the largest, then c must be the largest
else:
    largest = c

print("Largest number is:", largest)