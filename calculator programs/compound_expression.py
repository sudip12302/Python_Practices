''' Take thiree humbers as input and calculate sum , average and expression=(a+b)^2+(b+c)^2'''
#taking input of three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

#calculating sum
sum = a + b + c
print("The sum of the three numbers is ",sum)

#calculating average
avg = sum/3
print("The average of the three numbers is ",avg)   

#calculating expression
expression = (a+b)**2 + (b+c)**2
print("The result of expression (a+b)^2+(b+c)^2 is ",expression)

