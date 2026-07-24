'''given below is a 3*3 matrix a use 2d lists to represent the matrix in a python script , then find out the elements of the matrix which are divisible by 2 ans 3 also find out the max and min element of matrix 
a[24,3,6][8.12.18][2,66,7]'''
A = [[24, 3, 6], [8, 12, 18], [2, 66, 7]]
list1 = []
for row in A: #for ascessing each row of the matrix
    for element in row: # for ascessing each element of the row
        if element % 2 == 0 and element % 3 == 0: # checking the condition for divisibility by 2 and 3
            list1.append(element) # adding the element to the list if it satisfies the condition
print("Elements of the matrix that are divisible by 2 and 3:", list1)
flattened_A = [element for row in A for element in row] # flattening the matrix A to single line
max_element = max(flattened_A) # finding the maximum element in the flattened matrix
min_element = min(flattened_A) # finding the minimum element in the flattened matrix
print("Maximum element in the matrix:", max_element)
print("Minimum element in the matrix:", min_element)