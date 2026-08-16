''' To take the subject name and marks as inout and display total marks ,percentage and avg marks '''
# taking input of subject and its respective marks
sub1 = input("Enter the name of first subject")
mark1 = float(input("Enter the marks for first subject"))
              
sub2 = input("Enter the name of second subject")
mark2 = float(input("Enter the marks for second subject"))
              
sub3 = input("Enter the name of third subject")
mark3 = float(input("Enter the marks for third subject"))
              
sub4 = input("Enter the name of forth subject")
mark4 = float(input("Enter the marks for forth subject"))

#Calculating total marks
total_marks = mark1+mark2+mark3+mark4
print("Total obtained marks is ",total_marks)

#calculationg average marks
avg_marks=total_marks/4
print("The average marks is ",avg_marks)
 
 #calculating percentage
percentage=(total_marks/400)*100
print("The percentage is ",percentage,"%")