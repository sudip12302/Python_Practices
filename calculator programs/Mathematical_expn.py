''' Take 4 numbers as a,b,c&d and calculate the expression (a+b)^2+(b+c)^2+(c+d)^2+(a+d)^2 and average of 4 numbers'''
a= float(input("Enter the first number: "))
b= float(input("Enter the second number: "))
c= float(input("Enter the third number: "))
d= float(input("Enter the fourth number: "))
#calculating expression
expression = (a+b)**2 + (b+c)**2 + (c+d)**2
print("The result of expression (a+b)^2+(b+c)^2+(c+d)^2+(a+d)^2 is ",expression)
#calculating average
average = (a + b + c + d) / 4
print("The average of 4 given numbers is ",average)