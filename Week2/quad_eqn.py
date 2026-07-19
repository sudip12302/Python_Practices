import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

result1= (-b + math.sqrt(d)) / (2*a)
result2 = (-b - math.sqrt(d)) / (2*a)

print("First solution =", result1)
print("Second solution =", result2)
