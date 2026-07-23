# take inout form user list them in lsit and find the unique elements in the list
n = int(input("Enter the number of elements in the list: "))  
numbers = []
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

unique_numbers = set(numbers)  # Convert the list to a set to get unique elements
print("The unique elements in the list are:", unique_numbers)  # Print the unique elements