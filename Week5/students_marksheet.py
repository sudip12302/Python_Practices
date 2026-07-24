'''write a program that takes input as names and marks obtained on a certain subject of n students.
 then the data must be stored in a dictionary with the names as keys and marks as values. then print out all
   the names and marks of the students'''

n = int(input("Enter the number of students: "))
students_marksheet = {}
for i in range (n):
    name = input("Enter the name of student :")
    marks = int(input("Enter the marks obtained by {}: ".format(name)))
    students_marksheet[name] = marks
    

    
for name, marks in students_marksheet.items():
    print("Name:", name, "Marks:", marks)