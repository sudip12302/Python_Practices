''' a program that creates a 2d list having m number of rows and n number of columns, all the elements
in the diagonal should be 1 and the rest of the elements should be 0. the elements aboove the diagonal 
should be 2 and the elements below the diagonal should be 3. value of m and n should be taken from the user.''' 
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
Matrix = []
for i in range(m):
    row  = []
    for j in range(n):
        if i == j:
            row.append(1)
        elif i < j:
            row.append(2)
        else:
            row.append(3)   
    Matrix.append(row)
print(Matrix)


