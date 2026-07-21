''' a program that asks the user to input the current day of the week, if
it’s a weekday the program should print out “Happy weekday! Work
hard!” else the output should be “Enjoy your weekend! '''

str = input("Enter the current day of the week: ")  # Ask the user to enter the current day of the week
if str in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:  # Check if the entered day is a weekday
    print("Happy weekday! Work hard!")  # If it is a weekday, print the message for weekdays
   
else:
    print("Enjoy your weekend!")  # If it is not a weekday, print the message for weekends