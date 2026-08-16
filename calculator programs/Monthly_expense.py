''' To calculate the monthly expensees and yearly expenses'''
food = float(input("Enter the expenses for food in Rs: "))
clothes = float(input("Enter the expense for clothing in Rs: "))
education = float(input("Enter the  expense for education in Rs: "))
transport = float(input("Enter the expense for transport in Rs: "))
others = float(input("Enter the other expenses in Rs: "))
monthly_expenses = food+clothes+education+transport+others
print("The monthly expense is Rs",monthly_expenses)
yearly_expenses = monthly_expenses*12
print("The yearly expense is Rs",yearly_expenses)
