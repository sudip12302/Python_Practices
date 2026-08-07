''' to read, store and write the data of student in a 2D list, read data from students.txt file and write the data which overrides the previous data '''

def read_data():
    with open('students.txt', 'r') as file:
        data = file.readlines()
    students = []
    for line in data:
        if line.strip():  # skip empty lines
            parts = line.strip().split(', ')
            id, name, marks = parts
            students.append([id, name, int(marks)])
    return students

def add_student(students, id, name, marks):
    students.append([id, name, marks])

def update_marks(students):
    id = input("Enter student ID: ")
    found = False
    for student in students:
        if student[0] == id:
            found = True
            try:
                new_marks = int(input("Enter new marks: "))
                student[2] = new_marks
                print("Marks updated successfully.")
            except ValueError:
                print("Invalid marks. Please enter a numeric value.")
            break
    if not found:
        print("Student ID not found.")

def write_data(students):
    with open('students.txt', 'w') as file:
        for student in students:
            file.write(f"{student[0]}, {student[1]}, {student[2]}\n")

# Main execution
students = read_data()
print("Initial students data:")
for student in students:
    print(student)

while True:
    print("\nMenu:")
    print("1. Add student")
    print("2. Update marks")
    print("3. Display students")
    print("4. Save and exit")
    choice = input("Choose an option: ")
    if choice == '1':
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        try:
            marks = int(input("Enter student marks: "))
            add_student(students, id, name, marks)
            print("Student added successfully.")
        except ValueError:
            print("Invalid marks. Please enter a numeric value.")
    elif choice == '2':
        update_marks(students)
    elif choice == '3':
        print("Current students:")
        for student in students:
            print(student)
    elif choice == '4':
        write_data(students)
        print("Data saved to students.txt. Exiting.")
        break
    else:
        print("Invalid choice. Please try again.")
