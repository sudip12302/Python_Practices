''' Take input of unit consumed and calculate electricity bill '''
unit_consumed = int(input("Enter unit consumed: "))
charge_per_unit = 12
bill_amount = unit_consumed * charge_per_unit
service_charge = 100
total_bill = bill_amount + service_charge
print("Electricity Bill Amount: Rs.",total_bill)