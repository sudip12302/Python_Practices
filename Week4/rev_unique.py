# take input from user list them in list and find the unique elements in reverse order

n = int(input("Enter the number of elements in the list: "))  
numbers = []

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

unique_numbers = set(numbers)     # Get unique elements
unique_numbers = list(unique_numbers)  # Convert set back to list
unique_numbers.sort()
unique_numbers.reverse()


print("The unique elements in the list are:", unique_numbers)