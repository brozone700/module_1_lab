"""
Creator: Christian Livingston
StudentGPATester.py
Accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.
"""
while True:
    StudentLastName = input("Students's last name: ")
    if StudentLastName == "ZZZ":
        break
    StudentFirstName = input("Students's first name: ")
    StudentGPA = float(input("Student's GPA: "))
    if StudentGPA >= 3.5:
        print(f"{StudentFirstName} {StudentLastName} has made the Dean's List.")
    elif StudentGPA >= 3.25:
        print(f"{StudentFirstName} {StudentLastName} has made the Honor Roll.")
    else:
        print(f"{StudentFirstName} {StudentLastName} has made neither the Dean's List nor the Honor Roll.")