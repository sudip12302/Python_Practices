#write a program to print all the elemetents from a list which are divisible by 2 and 3
a = [2,3,6,8,9,12,15,18,24,22,23,112] 
for i in a:
    if i % 2 == 0 and i % 3 == 0:
        print(f"the number {i} is divisible by 2 and 3")
       