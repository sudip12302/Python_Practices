#to take input from users in list and find the odd and even numbers in the list and their sum separately
n = int(input("Enter the number of elements in the list: "))
numbers = [] #initialize an empty list to store the numbers
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num) #append the input number to the list
     
even_sum = 0 #initialize the sum of even numbers to 0
odd_sum = 0 #initialize the sum of odd numbers to 0
for num in numbers:
    if num % 2 == 0: #check if the number is even
        even_sum = even_sum + num #update the sum of even numbers by adding the current number
    else:
        odd_sum = odd_sum + num #update the sum of odd numbers by adding the current number
print("Sum of even numbers in the list:", even_sum)
print("Sum of odd numbers in the list:", odd_sum)
