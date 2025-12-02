"""
Day 03 — Conditional Statements & Loops
Author: Mynkq7
Date: 2025

Topics Covered:
- If / Elif / Else
- Logical operators
- Membership operators
- For loops
- Looping through lists
- Looping through strings
"""

# -------------------------
# Basic Logical Statement
# -------------------------

condition = 5 > 4  # Always true

if condition:
    print("Yeah you are right, 5 is always greater than 4")

print("So how are you?")

# -------------------------
# If / Elif / Else
# -------------------------

temperature = 40

if temperature > 30:
    print("It is hot outside")
elif temperature > 24:
    print("It's warm outside")
elif temperature > 10:
    print("It's cold outside")
elif temperature > 0:
    print("It's very cold outside")
else:
    print("It's freezing outside")

# -------------------------
# Logical Operators
# -------------------------

x = 100
y = 50
c = 200

if y < x and c > x:
    print("Yes, y is smaller than x but x is smaller than c")

# -------------------------
# Membership Operators
# -------------------------

words = ["wood", "tree", "car", "truck"]

if "wood" not in words:
    print("The word 'wood' is not present in the list")
elif "wood" in words:
    print("Wood is present in the list")

# -------------------------
# For Loops
# -------------------------

container = [1,2,3,4,5,6,7,8,9,10]

for number in container:
    print(number)

# -------------------------
# Iterating Over a List
# -------------------------

list_of_colors = [
    "orange", "green", "blue", "red",
    "black", "white", "purple", "yellow"
]

for color in list_of_colors:
    print(f"Here is your color: {color}")

# -------------------------
# Looping Through a String
# -------------------------

text = "Im a hacker"

for character in text:
    print(character)
