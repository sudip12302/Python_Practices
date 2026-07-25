'''a program to store the values of the matrix given below and find the sum of the diagonal elements , 
the sum of all elements above the diagonal and the sum of all elements below the diagonal,and ifnd min and max
element in the matrix. the matrix is given below:[[1,2,3],[8,9,4],[7,6,5]]'''


A = [[1,2,3],[8,9,4],[7,6,5]]
sum_diagonal = 0
# Calculate sum of diagonal elements (where i == j)
for i in range(len(A)):
    sum_diagonal += A[i][i]
print("Sum of diagonal elements:", sum_diagonal)
# Initialize sum for elements above the diagonal
sum_above_diagonal = 0
# Calculate sum of elements above the diagonal (where j > i)
for i in range(len(A)):
    for j in range(i+1, len(A[i])): # j > i means we are above the diagonal
        sum_above_diagonal =sum_above_diagonal+A[i][j]

print("Sum of elements above the diagonal:", sum_above_diagonal)

# Initialize sum for elements below the diagonal
sum_below_diagonal = 0

# Calculate sum of elements below the diagonal (where j < i)
for i in range(len(A)):
    for j in range(i): # j < i means we are below the diagonal
        sum_below_diagonal = sum_below_diagonal + A[i][j]

print("Sum of elements below the diagonal:", sum_below_diagonal)        

# Initialize min and max with the first element
min_element = A[0][0]
max_element = A[0][0]

# Find minimum and maximum elements in the matrix
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] < min_element:
            min_element = A[i][j]
        if A[i][j] > max_element:
            max_element = A[i][j]

print("Minimum element:", min_element)
print("Maximum element:", max_element)