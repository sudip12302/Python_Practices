''' write a program that takes input from users as a string of numbers then calculate the sum of all the numbers and print it out'''
def sum_of_numbers(numbers):   
    total_sum = 0
    for num in numbers:
        total_sum += float(num) #convert each number to a float and add it to the total sum
    return total_sum

numbers=input("Enter numbers separated by space: ")
numbers_list = numbers.split() #split the input string into a list of strings
result = sum_of_numbers(numbers_list)
print(f"Sum of all numbers in the string: {result}")


