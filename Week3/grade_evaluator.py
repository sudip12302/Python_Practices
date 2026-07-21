#TO take input of marks obtained in 5 subjects and calculate total, average and grade 
name = input("Enter the name of the student: ")

subjects = ["Math", "Science", "English", "History", "Art"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter marks obtained in {subject}: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / len(subjects)

if average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
elif average_marks >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Student Name: {name}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Grade: {grade}")
