'''takes N number of integers as input and puts them in a list. Then it should find out the maximum
 and minimum number from thelist and print them out. The whole list must also be printed out'''
n = int(input("Enter the number of elements in the list: "))  # Ask the user to enter the number of elements in the list
numbers = []  # Initialize an empty list to store the numbers
for i in range(n):  # Loop n times to get the numbers from the user
    num = int(input("Enter a number: "))  # Ask the user to enter a number and convert it to an integer
    numbers.append(num)  # Add the entered number to the list
    sorted_numbers = sorted(numbers)  # Sort the list of numbers in ascending order
max_num = sorted_numbers[-1] # Initialize max_num to the last element of the sorted list
min_num = sorted_numbers[0] # Initialize min_num to the first element of the sorted list

print("The list of numbers is:", numbers)  # Print the list of numbers
print("The maximum number is:", max_num)  # Print the maximum number
print("The minimum number is:", min_num)  # Print the minimum number