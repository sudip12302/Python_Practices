''' Take input of products and display results step by step '''

# Product 1
product1 = input("Enter name of first product: ")
cost1 = float(input("Enter cost price of first product in Rs: "))
sell1 = float(input("Enter selling price of first product in Rs: "))
profit1 = sell1 - cost1
print("Profit for", product1, "is Rs",profit1)

# Product 2
product2 = input("Enter name of second product: ")
cost2 = float(input("Enter cost price of second product in Rs: "))
sell2 = float(input("Enter selling price of second product in Rs: "))
profit2 = sell2 - cost2
print("Profit for", product2, "is Rs",profit2)

# Product 3
product3 = input("Enter name of third product: ")
cost3 = float(input("Enter cost price of third product in Rs: "))
sell3 = float(input("Enter selling price of third product in Rs: "))
profit3 = sell3 - cost3
print("Profit for", product3, "is Rs",profit3)

# Totals
total_cost = cost1 + cost2 + cost3
print("\nTotal Cost Price: Rs", total_cost)

total_selling = sell1 + sell2 + sell3
print("Total Selling Price: Rs", total_selling)

total_profit = total_selling - total_cost
print("Total Profit: Rs", total_profit,)

profit_percentage = (total_profit / total_cost) * 100
print("Profit Percentage:", profit_percentage, "%")