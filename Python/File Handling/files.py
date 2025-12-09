"""
File Handling & OS Module  
Author: Mynkq7  
Date: 2025
"""

import os

# Flags
# r - Read 
# w - Write 
# a - Append
# x - Create 
# b - Binary
# t - Text

# Open a file 
f = open("names.txt")

# Read the first 4 characters of the file and print it 
print(f.read(4))

# Read the line of the file 
print(f.readline())

# Print the second line of the file
print(f.readline())

# Print the third line of the file
print(f.readline())

# Looping through the file line by line 
for line in f:
    print(line)

# Closing the file 
f.close()

# Try, except, finally
# Try to open a file
try:
    f = open("names.txt")
    # Read the file and print its content
    print(f.read())
# Except if the file could not be opened
except: 
    # Print an error message 
    print("The file could not be opened")
# Finally close the file 
finally:
    f.close()

# Appending to a file 
# Open the file in append mode
f = open("names.txt", "a")
# Write to the file
f.write("jerry")
f.write("watson")
# Close the file
f.close()

# Reading the updated appended file 
f = open("names.txt", "r")
# Print the content of the file 
print(f.read())

# Overwriting a file 
f = open("context.txt", "w")
# Write to the file 
f.write("added some new context")
# Closing the file 
f.close()

# Reading the overwritten file
f = open("context.txt")
print(f.read())

# Open a file for writing and create it if it does not exist
f = open("nex-file.txt", "w")
f.close()

# If the file does not exist
if not os.path.exists("newfile.txt"):
    # Printing this message
    print("The file does not exist, creating it now")
    # Creating new file
    os.mknod("newfile.txt")

# If the file exists
if os.path.exists("nex-file.txt"): 
    # Print this message
    print("We are removing the file now which is nex-file.txt")
    # Remove the file
    os.remove("nex-file.txt")

# With and as statements 
# Open a file using with and as statements
with open("names.txt") as f:
    # Read the file and store inside newly created variable "content"
    content = f.read()

# Print the content of the file
print(content)