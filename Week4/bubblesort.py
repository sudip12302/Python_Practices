# to take input of a list of numbers and sort them using bubble sort algorithm
n = int(input("Enter the number of elements in the list: "))
numbers = []

while len(numbers) < n:
    num = int(input("Enter a number: "))
    numbers.append(num)

# bubble sort algorithm
is_sorted = False

while is_sorted == False:
    num_swaps = 0

    for i in range(1, len(numbers)):
        if numbers[i-1] > numbers[i]:
            tmp = numbers[i-1]
            numbers[i-1] = numbers[i]
            numbers[i] = tmp
            num_swaps += 1

    if num_swaps == 0:
        is_sorted = True

print("Sorted list:", numbers)