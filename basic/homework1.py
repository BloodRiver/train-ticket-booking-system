import os

def determine_grade(marks):
    if marks >= 90:
        return "A*"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"


filename = "students.txt"

# if os.path.exists("student.txt") != True:
# if os.path.exists("student.txt") == False:
if not os.path.exists(filename):  # If the students.txt does NOT already exist
    my_file = open(filename, "w")  # open the file in write mode
    my_file.write("Student ID, Name, Chemistry Marks, Physics Marks, Computer Science Marks\n")
else:  # if the file already exists
    my_file = open(filename, "r") # open the file in read mode 

    line = my_file.readline()  # read ONE line

    if line == "Student ID, Name, Chemistry Marks, Physics Marks, Computer Science Marks\n":
        my_file.close()
        header_exists = True
    else:
        header_exists = False
    
    my_file = open(filename, "a")

    if not header_exists:
        my_file.write("Student ID, Name, Chemistry Marks, Physics Marks, Computer Science Marks\n")

num_students = int(input("How many students in the class?: "))

for i in range(num_students):
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    chemistry_marks = float(input("Enter Chemistry Marks: "))
    chemistry_grade = determine_grade(chemistry_marks)

    physics_marks = float(input("Enter Physics Marks: "))
    physics_grade = determine_grade(physics_marks)

    computer_science_marks = float(input("Enter Computer Science Marks: "))
    computer_science_grade = determine_grade(computer_science_marks)

    my_file.write(f"{student_id}, {student_name}, {chemistry_grade}, {physics_grade}, {computer_science_grade}\n")

my_file.close()