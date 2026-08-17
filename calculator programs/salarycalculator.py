''' taking input from user  calculate hra , dae and calculating gross salary '''
basic = float(input("Enter basic salary: "))
hra = basic * 0.10
print("HRA: ", hra)
da = basic * 0.05
print("DA: ", da)
gross_salary = basic + hra + da
print("Gross Salary: ", gross_salary)