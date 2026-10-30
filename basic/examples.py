# Global Variable
my_string = "Hello World"

class Student:
    name = ""
    age = 0
    email = ""

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        print(my_string)

    # Override
    def __str__(self):
        return f"<Student: {self.name}, {self.age}, {self.email}>"



def function():
    print("Inside the function, my_string:")
    print(my_string)  # it works
    local_variable = "This is a local Variable"

    print("Inside the function")
    print(local_variable)

s1 = Student("Sajeed", 24, "sag.arnob@gmail.com")
s2 = Student("Shahrear", 27, "shahrear@gmail.com")

output_string = "Student Info: " + str(s1)

print(output_string)

print(s2)

function()
print("--------------------------")
print("Outside function")
print(my_string)
print("--------------------------")

print(s2.age)
print(age)
