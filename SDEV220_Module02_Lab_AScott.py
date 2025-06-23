#Angela Scott
#SDEV220_Module02_Lab_AScott
#Python Script for SDEV220, 1AH developed 23 JUN 2025. The application will accept a student's GPA as a string and convert it to a float number.
#The float data type will be used in an if-else statement that will determine if the student's GPA will qualify for the Deans's List (GPA of 3.5 or greater)
#The elif will determine if the student's GPA will qualify for the Honor Roll (GPA of 3.25 of greater)
#The else statement will default to print that the student does not qualify for awards.


import math

#accept data from user
student_name = input(str("Enter the student's name or enter 'ZZZ' to Quit: "))
while student_name != "ZZZ":
    
    student_gpa = input(str("Enter the student's GPA: "))
    #convert string to float
    student_gpa1 = (float(student_gpa))

#print(student_name)
#print(student_gpa1)


    #if-else statement
    if student_gpa1 >= 3.5:
        print(student_name, "is qualified for the Dean's List with a GPA of", student_gpa1)
    elif student_gpa1 >= 3.25:
        print(student_name, "is qualified for the Honor Roll.")
    else:
        print("This student's GPA does not qualify for additional awards.")
    break 