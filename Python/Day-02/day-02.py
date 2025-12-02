"""
Day 02 — Python Intermediate Basics
Author: Mynkq7
Date: 2025

Topics Covered:
- Tuples
- Sets
- Dictionaries
- Basic Operators
- String operations
- Membership operators
- Arithmetic & Comparison operators
"""

# -------------------------
# Tuples (Immutable Ordered Collection)
# -------------------------

empty_tuple = ()  # empty tuple
list_data = [0,1,2,3,4,5,6,7,8,9, 1,2,3,4,5,6,7,8,9]  # lists are mutable
data = (0,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9)       # tuples are immutable

nested_tuple = (
    (0,0,0),
    (1,2,3),
    (2,3,4)
)

# Accessing tuple elements
print(data[5])
print(data[3])
print(data[4])

# Slicing
print(data[:3])
print(data[3:])

# Tuple functions
print(len(data))
print(min(data))
print(max(data))
print(sum(data))
print(sorted(data))

# Count occurrences
print(data.count(4))
print(data.count(8))

# -------------------------
# Sets (Unordered, Unique Items)
# -------------------------

sett = {"A", "A", "B", "B", "C", "C", "D", "D"}
print(sett)  # duplicates are removed automatically

# Convert list → set, set → list
list_to_set = set(list_data)
set_to_list = list(sett)

print(list_to_set)
print(set_to_list)

# Set comparison methods
A = {1,2,3,4}
B = {3,4,5,6}

print(A.union(B))
print(A.intersection(B))
print(A.symmetric_difference(B))
print(A.issubset(B))
print(A.issuperset(B))

# -------------------------
# Dictionaries (Key → Value, Mutable)
# -------------------------

empty_dictionary = {}

items = {
    'name': 'mayank',
    'age': '21',
    'from': 'Delhi',
    'country': 'India',
    'favorite_color': 'black',
    'likes': 'Peace',
    'fav_food': 'chicken',
}

# Accessing dictionary values
print(items)
print(items["name"])
print(items["age"])
print(items["from"])
print(items["country"])
print(items["likes"])
print(items["favorite_color"])
print(items["fav_food"])

# Modifying data
items['name'] = 'Ramesh'
items['favorite_color'] = 'orange'
print(items)

# Membership operators
print('hobby' in items)
print('name' in items)
print('hobby' not in items)
print('name' not in items)

# Dictionary functions
print(len(items))
print(list(items.keys()))
print(list(items.values()))
print(items.pop('name'))

# -------------------------
# Basic Operators
# -------------------------

x = 10
y = 20
total = x + y

print(total)
print(x + y)

# -------------------------
# String Operations
# -------------------------

a = "Hello"
b = "world"

# Joining strings
combined = a + b
print(combined)
print(a + b)
print("The combined string is:", combined)

# Multiplying strings
print("Hello\n" * 5)

# -------------------------
# Membership Operators
# -------------------------

sentence = "so we are going to hit some pushups"

print("slap some pushups" in sentence)
print("hit some pushups" not in sentence)
print("hit some pushups" in sentence)

# -------------------------
# Equality Operators
# -------------------------

s_1 = "this is a cat"
s_2 = "this is a cat"
s_3 = "this is a rat"

print(s_1 == s_2)
print(s_1 == s_3)
print(s_1 != s_3)

# -------------------------
# Arithmetic Operators
# -------------------------

n_1 = 2
n_2 = 4

print("n_1 + n_2:", n_1 + n_2)
print("n_1 - n_2:", n_1 - n_2)
print("n_1 / n_2:", n_1 / n_2)
print("n_1 * n_2:", n_1 * n_2)
print("n_1 // n_2:", n_1 // n_2)
print("n_1 % n_2:", n_1 % n_2)
print("n_1 ** n_2:", n_1 ** n_2)

# -------------------------
# Comparison Operators
# -------------------------

print("n_1 > n_2:", n_1 > n_2)
print("n_1 < n_2:", n_1 < n_2)
print("n_1 == n_2:", n_1 == n_2)
print("n_1 >= n_2:", n_1 >= n_2)
print("n_1 <= n_2:", n_1 <= n_2)
print("n_1 != n_2:", n_1 != n_2)
