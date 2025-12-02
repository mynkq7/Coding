# Mixing Colors — simple style (no functions)
# Author: Mayank
# Day 03 mini-project

# Asking Inputs (normalize to lowercase and strip spaces)
color_1 = input("Enter first color (Red, Yellow, Blue): ").strip().lower()
color_2 = input("Enter second color (Red, Yellow, Blue): ").strip().lower()

# Keep original variable names similar to your style
first_color = color_1
second_color = color_2

# Supported colors list (for simple validation)
colors_bucket = ["red", "blue", "yellow"]

# Handle invalid inputs first
if first_color not in colors_bucket or second_color not in colors_bucket:
    print("Only 'red', 'blue', and 'yellow' are supported. Please try again.")
# Same color -> output that color
elif first_color == second_color:
    print(f"Mixing {first_color.title()} + {second_color.title()} results in {first_color.title()} (same color).")
# Mixing red and blue together
elif (first_color == "red" and second_color == "blue") or (first_color == "blue" and second_color == "red"):
    print("After mixing Red and Blue we get Purple.")
# Mixing yellow and red together
elif (first_color == "yellow" and second_color == "red") or (first_color == "red" and second_color == "yellow"):
    print("After mixing Yellow and Red we get Orange.")
# Mixing yellow and blue together
elif (first_color == "yellow" and second_color == "blue") or (first_color == "blue" and second_color == "yellow"):
    print("After mixing Yellow and Blue we get Green.")
# Fallback (shouldn't hit because of earlier checks)
else:
    print("Only blue, red, and yellow will work.")
