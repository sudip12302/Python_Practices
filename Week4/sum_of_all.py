# to take input of a list of numbers and find the sum of all the numbers in the list
n = int(input("Enter the number of elements in the list: "))
numbers = [] #initialize an empty list to store the numbers
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num) #append the input number to the list
total_sum = sum(numbers) #calculate the sum of all the numbers in the list using the built-in sum function
print("Sum of all numbers in the list:", total_sum)
