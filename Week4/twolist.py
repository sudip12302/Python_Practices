list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

combined = []   # new list to store result

i = 0  

# take elements alternately from both lists
while i < len(list1) and i < len(list2):
    combined.append(list1[i])  # add from list1
    combined.append(list2[i])  # add from list2
    i += 1  # move to next index

# if list1 still has elements left, add them
while i < len(list1):
    combined.append(list1[i])
    i += 1

# if list2 still has elements left, add them
while i < len(list2):
    combined.append(list2[i])
    i += 1

# print the final combined list
print(combined)