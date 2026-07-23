#wite a program that perform element wise additon on 2 list of numbers having the same length and output another list containing the sum
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = []  

i=0
while i < len(list1) and i < len(list2):
    result.append(list1[i] + list2[i])  # add sum of corresponding elements
    i += 1  
print(result) 