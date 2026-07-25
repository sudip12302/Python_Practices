''' a program that takes as input the name of students and marks obtained on a certain subject of N
students , then the data is stored in a dictionary with the names as the keys and the marks as the values.
 then find out the highest , lowest and average marks obtained by the students and print them all.'''
# Read input
n = int(input("Enter the number of students: "))
student_marks = {}
# Store student names and marks in a dictionary
for i in range(n):
    name = input("Enter the name of the student: ")
    marks = float(input("Enter the marks obtained by the student: "))
    student_marks[name] = marks

# Calculate highest, lowest, and average marks
highest_marks = max(student_marks.values())
lowest_marks = min(student_marks.values())
average_marks = sum(student_marks.values()) / len(student_marks)
# Output results
print("Highest marks:", highest_marks, )
print("Lowest marks:", lowest_marks, )
print("Average marks:", average_marks)