''' to calculate the travel cost '''
distance = float(input("Enter the distance to travel in kilometers: "))
expenses = float(input("Enter the expenses per kilometers: "))
days = int(input("Enter the number of days for the trip: "))
total_cost = distance * expenses * days
print("The total cost of the trip is:", total_cost)
