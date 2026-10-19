# Python Basics

## Data types

How many types of data are there?

Category | Explanation | Data Types (and Examples)
---------|------------------|-----------
Primitive Data Type | The most basic data type which exists on its own and can not be broken down into parts. | Integer, Float, Boolean, Character/Char (not directly in python) - one single alphabet/number/symbol a-z, A-Z, 0-9 or any special symbol. Example 'a' is a character, '@' is a character '5' is a character
Derived Data Type | Made up of two or more primitive data types | Date, Time
User-defined Data Type | Custom data type created by the programmer | Made using class keyword e.g. Student

Example of user-defined data type:
```py
class Student:
    name = ""
    student_id = ""
    email = ""
    cgpa = 0.0

    def __init__(self, my_name, student_id, email, cgpa):
        self.name = my_name,
        self.student_id = student_id
        self.email = email
        self.cgpa = cgpa


s1 = Student("Sajeed", "sag.arnob@gmail.com", "2121104", 3.5)

print(s1.name)
# Output: Sajeed
print(s1.email)
# Output: sag.arnob@gmail.com
```


## Mathematical Operators

Operator | Purpose
---------|--------
`+` | Addition
`-` | Subtraction
`*` | Multiplication
`/` | Division
`**` | Power (Exponential)
`%` | Modulus (Remainder of division)
`//` | Floor Division
+= | Addition to the same variable e.g. `counter += 10`
-= | Subtraction from the same variable e.g. `points -= 5`
*= | Multiplication to the same variable
/= | Division from the same variable

**Floor Division**: Round DOWN to the nearest integer. Example: 102 // 10; normally, 102 / 10 = 10.2, 102 // 10 = 10
Example: 109 / 10 = 10.9; 109 // 10 = 10
This means anything after the decimal point is ignored and only the integer part is kept.


## Logical/Boolean Operators

Operator | Purpose
---------|--------
and | The result is True only when both inputs are True otherwise False
or | The result is False only when both inputs are False otherwise True
not | The result is the opposite of the input


## Condition Checking (if-elif-else)
Syntax:
```
if (some condition):
    do something
elif above condition is false but this condition is true:
    do something else
elif above condition is false but this condition is true:
    do something else
elif above condition is false but this condition is true:
    do something else
else:
    if all above conditions are false, do this
```

Example:
```py

# Descending order of grade determination based on marks
marks = 86

if marks > 90:
    grade = "A"
elif marks > 80:
    grade = "A-"
elif marks > 70:
    grade = "B+"
else:
    grade = "F"


print(grade)
# Output: A-
```

```py
# Ascending order of grade determination based on marks
marks = 70

if marks < 45:
    grade = "F"
elif marks >= 45 and marks < 50:
    grade = "D"
elif marks >= 50 and marks < 55:
    grade = "D+"
elif marks >= 55 and marks < 60:
    grade = "C-"
elif marks >= 60 and marks < 65:
    grade = "C"
elif marks >= 65 and marks < 70:
    grade = "C+"
elif marks >= 70 and marks < 75:
    grade = "B-"
elif marks >= 75 and marks < 80:
    grade = "B"
elif marks >= 80 and marks < 85:
    grade = "B+"
elif marks >= 85 and marks < 90:
    grade = "A-"
elif marks >= 90:
    grade = "A"
```

## Looping/Iteration (Repeating the same thing over and over again)

Type of loop | Explanation
-------------|------------
Pre-condition loop | checks a condition before entering the loop (e.g. while counter < 10)
Post-condition loop | performs the loop first, then checks condition to decide whether to continue looping or not
Iterable object based loop | loop continues for as long as the iterable can provide elements (e.g. elements of an array or list)
Infinite Loop | When we don't know how many times to loop, we use infinite loop and break upon a certain condition


### Examples
**Pre-condition Loop**
```py
counter = 0

while counter < 10:
    print(counter)
    counter += 1

'''
Output:
0
1
2
3
4
5
6
7
8
9
'''
```

**Post-condition Loop**: Python does not have any post condition loop. Another programming language like JavaScript does.
Example:

```js
var counter = 10;

do
{
    console.log(counter);
    counter -= 1;
}
while(counter > 0);
```

How to implement post-condition loop in python:

```py
counter = 10

while True:  # infinite loop
    print(counter)
    counter -= 1

    if counter < 1:
        break  # out of the loop
```

**Iterable object/collection-based loop**

```py

'''
Basic syntax

for each_element in my_array:
    do something
'''

# Python list
student_names = ["Sajeed", "Mohammad", "Galib", "Shahrear", "Arnob"]

for each_student_name in student_names:
    print(each_student_name)

print("Loop has ended")

'''
Output:
Sajeed
Mohammad
Galib
Shahrear
Arnob
Loop has ended
'''
```

## Functions

A re-usable part of the code

2 types:
1. Named function
2. Anonymous function (lambda function)

Python is an object oriented programming language. This means that everything in python (except primitive data types) is an object. Even functions are treated as objects.
In other programming languages like C++, functions behave a little differently (not as objects).


### Function Definition

1. How to define a named function

```py
def my_function(parameter_1, parameter_2):
    body of the function

    return some value

# how to call function
my_function(argument1, argument2)
```

Example:
```py
def add(value1, value2):
    return value1 + value2


x = 5
y = 6

z = add(x, y)  # x + y

print(z)  # 11
```

---

2. Passing Default Arguments while defining a function

Example:
```py
def add(x, y, z):
    return x + y + z


print(add(6, 7))
# Error will occur because value for x and y are given but value for z is missing


# giving a default value to z
def add_alternate(x, y, z=5):
    return x + y + z

print(add_alternate(6, 7))
# Output: 18
# because if we do not give any value for z
# by default value of z is 5 as defined in the function
# Therefore, add(6, 7) means x=6, y=7, and z=5
# (default value given while defining the function)
# Therefore 6 + 7 + 5 = 18
```

---

3. Anonymous (Lambda) Function

```py

f = lambda x: (2 * x) + 3

def f(x):
    return (2 * x) + 3

print(f(5))
# Output: 13
```


---

### Different ways to call a function
1. Positional Argument

```py
def print_params(param1, param2):
    print("The value of param1 is", param1)
    
    print("The value of param2 is", param2)


print_params(5, 6)
'''
Output:
The value of param1 is 5
The value of param2 is 6
'''

print_params(6, 5)
'''
Output:
The value of param1 is 6
The value of param2 is 5
'''
```

**Why the position matters**

```py
def introduce(name, age):
    print("Hello! My name is " + name + " and I am " + str(age) + " years old")


# Calling the function
introduce("Sajeed", 24)
# Output: Hello! My name is Sajeed and I am 24 years old

introduce(24, "Sajeed")
# Error: TypeError: unsupported operand type 'int'
# Explanation introduce(24, "Sajeed")
# means introduce(name=24, age="Sajeed")
# "Hello! My name is " + name + ...
# "Hello! My name is " + 24
#                   ^ can not add integer to a string
```

2. Named parameter/argument
**Position does not matter if we specifically tell which parameter should have which value**
```py
def introduce(name, age):
    print("Hello! My name is " + name + " and I am " + str(age) + " years old")


# Calling the function
introduce(age=24, name="Sajeed")
# Output: Hello! My name is Sajeed and I am 24 years old
```

**Important**: If we start using named parameters, we can not also use positional arguments at the same time

Example:
```py
introduce(name="Sajeed", 24)  # Error
```

Explanation:
```py
def function(param1, param2, param3, param4):
    do something

# Calling the function
function(param3="some value", 4, 7, 11)  # Error
# Python will not know which value should go to param1, param2, and param4


# Positional Argument/Parameter
function(4, 7, "some value", 11)  # OK
```

## Python built-in Data Structures

- String
- Tuple
- List
- Set
- Dictionary

### String
In python, String and Character are the same thing but in reality a String is just many characters placed side-by-side one after another

**Example:** 'h' is a character 'e' is a character 'l' is a character 'l' is a character 'o' is a character but put the all together and it becomes the string: 'hello'

So basically, string is an array of characters.

In python, strings are **immutable** meaning that once we create a string, we cannot change the individual characters in that string.

**How to access individual characters in a string**

```py
    # String indices (singular: index)
            #012345678910
my_string = "hello world"

print(my_string)
# Output: hello world

print(my_string[0])
# Output: h
print(my_string[1])
# Output: e
print(my_string[2])
# Output: l
print(my_string[3])
# Output: l

print(my_string[7])
# Output: o


my_string[0] = 'y'  # ERROR: We can not change individual characters in a string

# Because string is immutable (READ ONLY)
# mutate = change
# mutable = can change
# immutable = can not change
```

#### String Concatenation
String concatenation means to add the beginning of one string to the end of another string.

**Example:**
```py
string1 = "i eat"
string2 = "rice"

result = string1 + string2

result2 = string1 + " " + string2

print(result)
# Output: i eatrice

print(result2)
# Output: i eat rice
```

#### Concatenating other values to a string
We can not use the `+` operator to add values of other data types to a string. We must at first convert that value to a string using the `str` function.

**Example**:
```py
name = "Sajeed"
age = 24
weight = 82.3
height = 170

print("Hello! My name is " + name + " and I am " + str(age) + " years old. I weigh " + str(weight) + " kilograms and my height is " + str(height) + " cm")
```

### Tuple
String is an array of characters meaning that the entire collection of characters is a single data type - `String`

But **Tuple** is an ordered collection of values. In python, data type does not matter so we can store different values of different data types in the same tuple.

**Example**:
```py
column_names = ("name", "age", "email", "height", "weight")

row_1 = ("Sajeed", 24, "sag.arnob@gmail.com", 170, 82.3)


print(row_1[0])
# Output: Sajeed
print(row_1[1])
# Output: 24
print(row_1[2])
# Output: sag.arnob@gmail.com
```

Just like Strings, tuples are **immutable** meaning that once we have put values in a tuple, we can NOT change those values in the same tuple.

**Example**
```py

row_1 = ("Sajeed", 24, "sag.arnob@gmail.com", 170, 82.3)

row_1[2] = "sajeed@gmail.com"  # ERROR: can not change tuple values

```

### Lists
Other programming languages have array as a built-in data structure.

Python does not have array. Instead, we use List.

Just like tuples, lists are ordered collections of data. We can store multiple values of different data types in the same list

**Example**
```py
student_data = ["Sajeed", 24, "sag.arnob@gmail.com", 170, 82.3]

print(student_data[0])
# Output: Sajeed
print(student_data[2])
# Output: sag.arnob@gmail.com
```

Difference between tuple and list is that Lists are **mutable** meaning that we CAN change individual elements in a list.

**Example**
```py
student_data = ["Sajeed", 24, "sag.arnob@gmail.com", 170, 82.3]

# No error because we CAN change individual elements of a list

student_data[0] = "Shahrear"
student_data[2] = "shahrear@gmail.com"


print(student_data)
# Output:
# ["Shahrear", 24, "shahrear@gmail.com", 170, 82.3]
```

Changing from tuple to list and back to tuple

**Example**
```py

# tuple
student_data = ("Sajeed", 24, "sag.arnob@gmail.com", 170, 82.3)

# Tuple is immutable

# 1. Convert to list and store in a temporary variable
temp_list = list(student_data)

# 2. Change the value in the list
temp_list[0] = "Shahrear"

# 3. Convert the temp_list to tuple, removing the previously existing tuple in student_data
student_data = tuple(temp_list)


# 4. student_data has now changed. Print to see the change
print(student_data)

# Output:
# ("Shahrear", 24, "sag.arnob@gmail.com", 170, 82.3)

```


### Set

Set is an unordered collection of unique elements.
This means the elements stored in the set may be stored in different orders at different runtimes.
It also means that the set data structure can not access elements via index since they are not stored in any particular order.

Sets are **mutable** because we can add or remove elements from the set.


**Example**
```py

email_ids = {"abc@email.com", "bcd@gmail.com", "def@yahoo.com",
 "def@yahoo.com", "abc@email.com", "bcd@gmail.com"}


print(email_ids)

# Output
# email_ids = {"abc@email.com", "bcd@gmail.com", "def@yahoo.com"}

# What happened? The duplicate elements have been removed.
```


### Dictionary

Uses a key-value pair to store elements in an unordered collection.
The keys of a dictionary are unique and cannot be duplicate.
Multiple values may be stored under the same key.

Think of an English Dictionary (Book of Word Meanings).

Dictionary is **mutable** because
<u>items</u> in the dictionary can be changed.

Key = Word
Value = Meaning/Description the word

**Syntax**
```
variable_name = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

Think of the above syntax as table containing ONLY ONE ROW

**Table Name:** variable_name

key1   | key2   | key3
-------|--------|-------
value1 | value2 | value3

**Example**

```py
shopping_item1 = {
    'item_name': 'Apple',
    'unit_price': 20.5,
    'quantity_in_stock': 500
}

print(shopping_item1)

'''
Output: {
    'item_name': 'Apple',
    'unit_price': 20.5,
    'quantity_in_stock': 500
}
'''

```

**Table Name:** shopping_item1
item_name | unit_price | quantity_in_stock
---------|----------|---------
Apple | 20.5 | 500


Let's see how to add more rows

```py
all_shopping_items = {
    'item_name': ['Apple', 'Banana', 'Cherry'],
    'unit_price': [20.5, 30.5, 50.5],
    'quantity_in_stock': [500, 600, 300]
}
```

**Table Name:** all_shopping_items

item_name | unit_price | quantity_in_stock
---|---|---
Apple | 500 | 20.5
Apple | 800 | 50.5
Banana | 600 | 30.5
Cherry | 300 | 50.5


#### Advantages of using dictionary

Consider the following code using lists:

```py

# Lists:
student_names = ["Sajeed", "Ahmed", "Mohammad", "Shahrear"]

student_ids   = ["1234", "2345", "3456", "4567"]

student_departments = ["CSE", "EEE", "BBA", "CSE"]

student_cgpas = [3.4, 2.4, 3.5, 2.9]

print(student_names[0])
# Output: Sajeed

print(student_ids[0])
# Output: 1234

print(student_departments[0])
# Output: CSE

```

index | student_names  | student_ids  |  student_departments | cgpas
--- | --- | --- | --- | ---
0 | Sajeed | 1234 | CSE | 3.4
1 | Ahmed | 2345 | EEE | 2.4
2 | Mohammad | 3456 | BBA | 3.5
3 | Shahrear | 4567 | CSE | 2.9

# Object Oriented Programming
## What is an object?
In reality, anything that physically exists is an object.
In programming, a user-defined block of data that is capable of performing certain tasks on its own is an object.
The object may also contain its own variables for data storage.

## How to make an object?

In programming, we create a **blueprint** that is used to create an object. To do so, we use the `class` keyword.
The word **class** can mean **category** or **user-defined data type**.

**Example**

```py
class Student:
    name = ""
    email = ""
    age = 0.0
    student_id = ""


s1 = Student()  # create a new Student object a.k.a instance

s2 = Student()

s3 = Student()

s4 = Student()
```

## The `type` function

```py
name = "Sajeed"
age = 24.5

print(type(name))
# Output: <class 'str'>

print(type(age))
# Output: <class: 'float'>


class Student:
    name = ""
    email = ""
    age = 0.0


s1 = Student()

print(type(s1))
# Output: <class 'Student'>
```

## Functions vs Methods
```py
class Student:
    name = ""
    email = ""
    student_id = ""
    age = 0.0

    def introduce(self):
        # This function is inside the Student class so it's a method

        print("My name is", self.name)


def add(x, y):
    # This function is NOT inside any class so it's a function

    return x + y


class Person:
    name = ""


print(add(5, 6))  # this will work because add function exists

introduce()  # This will NOT work because introduce function does not exist in this code

s1 = Student()

s1.name = "Sajeed"
s1.introduce()  # This will work because introduce function has been defined inside the Student class

p1 = Person()

p1.introduce()  # This will NOT work because introduce function does not exist inside the Person class
```

## The `__init__` method

Let's create a class

```py
class Student:
    name = ""
    email = ""
    age = 0.0
    student_id = ""
```

How do we set the variables of a Student instance?

```py
s1 = Student()
s1.name = "Sajeed"
s1.email = "sag.arnob@gmail.com"
s1.age = 24.5
s1.student_id = "2121104"
```

What if there was an easier way?

But first, let's see how methods work

```py
class Student:
    name = ""
    email = ""
    age = 0.0
    student_id = ""
    favorite_subject = ""

    def __init__(self, name, email):
        print("ghora chole tokbok tokbok")
        print("Creating an object of class Student")
        print("Name:", name)
        print("Email:", email)

    def introduce(self):
        print("I am introducing myself")


class Person:
    def __init__(self):
        print("I am alive")


s1 = Student("Sajeed", "sag.arnob@gmail.com")
p1 = Person()

```

Here is the easier way: (Next class)
