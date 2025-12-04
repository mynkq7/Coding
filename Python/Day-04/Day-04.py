"""
Day 04 — Loops Practice & Control Statements
Author: Mynkq7
Date: 2025

Topics Covered:
- Basic for loops
- Looping through lists
- Looping through strings
- continue statement
- Skipping specific items in loops
"""

# -------------------------
# Looping Through a List (Numbers)
# -------------------------
number_list = [1,2,3,4,5,6,7,8,9,10]

for num in number_list:
    print(f"Here is your number {num}")


# -------------------------
# Looping Through a List (Words)
# -------------------------
word_list = [
    "one", "two", "three", "four", "five", 
    "six", "seven", "eight", "nine", "ten"
]

for words in word_list:
    print(f"Here is your number: {words}")


# -------------------------
# Skipping a Single Letter Using continue
# -------------------------
Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in Alphabets:
    if letter == "M":
        print("Removing letter M")
        continue  # skip printing M
    print(f"Here is your Alphabet: {letter}")


# -------------------------
# Skipping Multiple Letters Using continue
# -------------------------
Alphabets_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_to_skip = "BFJNQ"  # letters we don't want

for newwords in Alphabets_2:
    if newwords in letters_to_skip:
        print(f"Removing unwanted letter: {newwords}")
        continue  # skip these letters
    print(f"Here is your Letter {newwords}")