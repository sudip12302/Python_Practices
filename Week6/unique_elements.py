# to find unique elements in a list adn sort by descending order
list1 = [1,1,2,3,3,4,4,5,6,5,6]
unique_elements = []
for element in list1:
    if element not in unique_elements:
        unique_elements.append(element)
        sorted_elements = sorted(unique_elements, reverse=True)
print(sorted_elements)
