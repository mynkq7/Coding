"""
Guessing Game — Day 03 Mini Project
Author: Mayank
Date: 2025

Description:
A simple number guessing game that checks the user's guess
and prints responses based on how close the guess is.
"""

# -------------------------
# Secret Number
# -------------------------
secret = 7  # The correct number user must guess

# -------------------------
# User Input
# -------------------------
user_guess = int(input("Guess a number: "))

# -------------------------
# Game Logic
# -------------------------

if user_guess == secret:
    print("🎉 Correct! You guessed the number!")
elif user_guess < 3:
    print("❌ Way too low!")
elif user_guess < 5:
    print("⬆️ Too low! Try a bit higher.")
elif user_guess < secret:
    print("Almost there! Aim slightly higher.")
elif user_guess > 10:
    print("❌ Way too high!")
elif user_guess > secret:
    print("⬇️ Too high! Aim lower.")
else:
    print("Invalid input")
