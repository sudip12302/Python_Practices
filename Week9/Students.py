class Students():
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english
    
    def get_lastname(self):
        """Returns the last name of the student"""
        return self.name.split()[-1]
    
    def avg_marks(self):
        """Returns the average marks of the student"""
        return (self.maths + self.science + self.english) / 3


# Test the class
S1 = Students("John Smith", 85, 90, 80)
print(f"Student Name: {S1.name}")
print(f"Last Name: {S1.get_lastname()}")
print(f"Average Marks: {S1.avg_marks()}")