'''take N numbers as input from a user and puts them in a list. Then the program should find out the sum of
all the odd numbers and the sum of all the even numbers from the list and print them out'''
n = int(input("Enter the number of elements in the list: "))  # Ask the user to enter the number of elements in the list
numbers = []  # Initialize an empty list to store the numbers
for i in range(n):  # Loop n times to get the numbers from the user
    num = int(input("Enter a number: "))  # Ask the user to enter a number and convert it to an integer
    numbers.append(num)  # Add the entered number to the list

odd_sum = 0
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of odd numbers:", odd_sum)
print("Sum of even numbers:", even_sum)