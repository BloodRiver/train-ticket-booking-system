# # # Global Variable
# # my_string = "Hello World"

# # class Student:
# #     name = ""
# #     age = 0
# #     email = ""

# #     def __init__(self, name, param_age, param_email):
# #         self.name = name
# #         self.age = param_age
# #         self.email = param_email
# #         print(my_string)

# #     # Override
# #     def __str__(self):
# #         return f"<Student: {self.name}, {self.age}, {self.email}>"

# #     def introduce(self):
# #         print("Hello! My name is ", self.name)




# # s1 = Student("Sajeed", 24, "sag.arnob@gmail.com")
# # s2 = Student("Shahrear", 27, "shahrear@gmail.com")


# # class Example:
# #     def __init__(self):
# #         print("Example object has been created!")


# # obj = Example()


# # class ChineseFoodChef:
# #     # These recipe books are for Chinese Food Chefs only

# #     # Recipe 1
# #     def cook_fried_rice(self):
# #         print("Cooking Fried Rice")

# #     # Recipe 2
# #     def cook_fried_chicken(self):
# #         print("Cooking Fried Chicken")


# # class BangaliFoodChef:

# #     # Object Oriented Programming Concept: __init__ is constructor
# #     def __init__(self, chef_name):
# #         self.name = chef_name

# #     # These recipe books are for Bangali Food Chefs only

# #     # recipe 1
# #     def cook_rice(self):
# #         print(self.name, "is cooking rice")
    
# #     # recipe 2
# #     def cook_alu_bhorta(self):
# #         print(self.name, "is cooking alu bhorta")


# # # Common recipe book. Can be used by all
# # def make_biriyani():
# #     print("Making Biriyani")


# # make_biriyani()

# # chef1 = BangaliFoodChef("Rahim")  # hired/created a BangaliFoodChef
# # chef1.cook_rice()

# # chef2 = BangaliFoodChef("Karim")
# # chef2.cook_alu_bhorta()


# # # def function():
# # #     print("Inside the function, my_string:")
# # #     print(my_string)  # it works
# # #     local_variable = "This is a local Variable"

# # #     print("Inside the function")
# # #     print(local_variable)

# # # output_string = "Student Info: " + str(s1)

# # # print(output_string)

# # # print(s2)

# # # function()
# # # print("--------------------------")
# # # print("Outside function")
# # # print(my_string)
# # # print("--------------------------")

# # # print(s2.age)
# # # print(age)


# my_string = "Hello World"


# class ExampleClass:
#     some_variable = "Test:" + my_string

#     def do_something(self):
#         print(self.some_variable)
#         do_something_local_variable = 5
#         print(my_string + " came from a global variable")

#     another_variable = "something is " + str(do_something_local_variable)  # Error


# def myFunction():
#     my_local_variable = "Some value"
#     print("Inside myFunction:", my_local_variable)
#     print(my_string, "can also be found here")


# def anotherFunction():
#     print(my_local_variable)  # Error


# print(ExampleClass.some_variable)

# instance = ExampleClass()
# instance.do_something()


# print("In the main Python Code:", my_string)
# myFunction()
# # print(my_local_variable)


class Student:
    # Class level attribute
    # common variable available for all instances of the same class
    department = "CSE"

    def __init__(self, name):

        # self.variable -> instance level variable
        # exists only for one instance and is different for each instance
        self.name = name


# class CSEStudent:
#     core_courses = ["CSE201", "CSE203", "CSE204", "CSE213"]
#     major_courses = ["CSE309", "CSE464"]

#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id



# cse_student1 = CSEStudent("Sajeed", "2121104")
# cse_student2 = CSEStudent("Shahrear", "1234567")

# print("CSEStudent.core_courses:", CSEStudent.core_courses)
# print("cse_student1.name:", cse_student1.name)
# print("cse_student2.name:", cse_student2.name)
# print("cse_student1.core_courses:", cse_student1.core_courses)
# print("cse_student2.core_courses:", cse_student2.core_courses)

# CSEStudent.core_courses = ["CSE201", "CSE203", "CSE204", "CSE213", "CSE211"]

# print("CSEStudent.core_courses:", CSEStudent.core_courses)
# print("cse_student1.core_courses:", cse_student1.core_courses)
# print("cse_student2.core_courses:", cse_student2.core_courses)


class FamilyMember:
    common_fund = 0

    def __init__(self, name):
        self.name = name
        self.personal_fund = 0


f1 = FamilyMember("Shahrear")
f2 = FamilyMember("Lovely")
f3 = FamilyMember("Saifur")

print("Common Fund:")
print(FamilyMember.common_fund)
print(f1.common_fund)
print(f2.common_fund)
print(f3.common_fund)
f3.__class__.common_fund += 50000
print("Common Fund after Uncle adding 50,000 taka")
print(f3.common_fund)
print(f3.name)
print(f1.name)
print("f1.common_fund:", f1.common_fund)


# s1 = Student("Sajeed")
# print(s1.department)

# print(Student.department)
# Student.department = "EEE"
# print(Student.department)
# print(s1.name)
# print(Student.name)
