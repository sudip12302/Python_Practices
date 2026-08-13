a=[[1,2,3],[23,43,54],[54,65,76,]]

for i in range(len(a)):
    for j in range(len(a[i])):
        min_element = a[0][0]
        if a[i][j] < min_element:
            min_element = a[i][j]
print(min_element)