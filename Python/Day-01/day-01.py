"""
Day 01 — Python Basics
Author: Mynkq7
Date: 2025

Topics Covered:
- Variables
- Print statements
- f-strings
- Data types
- Type checking
- Type conversion
- User input
- Lists & list operations
"""

# -------------------------
# Variables and Values
# -------------------------
variable_1 = "First Variable"
variable_2 = "Second Variable"
variable_3 = "Third Variable"
variable_4 = "Fourth Variable"

# Printing variables
print(variable_1)
print(variable_2)
print(variable_3)
print(variable_4)

# -------------------------
# f-Strings (Formatted Strings)
# -------------------------
print("Here are our variables:")
print(f"This is our {variable_1}")
print(f"This is our {variable_2}")
print(f"This is our {variable_3}")
print(f"This is our {variable_4}")

# -------------------------
# Data Types
# -------------------------
string_example = "This is our string"
integer_example = 9
float_example = 3.15
boolean_example = True
none_example = None

# Checking data types
print(type(string_example))
print(type(integer_example))
print(type(float_example))
print(type(boolean_example))
print(type(none_example))

# -------------------------
# Type Conversion
# -------------------------
integer_to_string = str(integer_example)
float_to_string = str(float_example)

print(integer_to_string)
print(float_to_string)

# -------------------------
# Inputs and Data Operations
# -------------------------
toffee = input("Enter how many toffees you have: ")
toffee_friend = input("Enter how many toffees your friend has: ")

num_1 = int(toffee)
num_2 = int(toffee_friend)
total = num_1 + num_2

print(f"You both have {total} toffees in total.")

# -------------------------
# Lists
# -------------------------
fruits = ["apple", "mango", "banana", "papaya"]

# Accessing elements by index
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# List slicing
print(fruits[0:3])   # first 3 fruits
print(fruits[1:3])   # index 1 to 2

# Built-in list functions
print(len(fruits))

fruits.append("avocado")
fruits.append("strawberry")
fruits.append("litchi")
fruits.append("guava")

fruits.remove("apple")

print(fruits)
