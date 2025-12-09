import os
# flags 
# r - read 
# w - write 
# a - append
# x - create 
# b - binary
# t - text
# open a file 
f = open("names.txt")
# read the file and print its content 
# print(f.read())
# Read the first 4 characters of the file and print it 
print(f.read(4))
# Read the line of the file 
print(f.readline())
# print the second line of the file
print(f.readline())
# print the third line of the file
print(f.readline())

# looping though the file line by line 
for line in f:
    print(line)
# closing the file 
f.close()

# try =, except, finally
# try to open a file
try:
    f = open("names.txt")
 # read the file and print its content
    print(f.read())
# except if the file could not be opened
except: 
# Print an error message 
    print("the file could not be opened")
# finally close the file 
finally:
    f.close()

# appending to a file 
# open the file in append mode
f = open("names.txt", "a")
# write to the file
f.write("jerry")
f.write("watson")
# close the file
f.close()
# reading the updated appended file 
f = open("names.txt", "r")
# print the content of the file 
print(f.read())

# Overwriting a file 
f = open("context.txt", "w")
# write to the file 
f.write("added some new context")
# closing the file 
f.close()
# reading the overwritten file
f = open("context.txt",)
print(f.read())
# closing the file 

# open a file for writing and create it if it does not exist
f = open("nex-file.txt", "w")
f.close

# if the file does not exist
if not os.path.exists("newfile.txt"):
    # printing this message
    print("the file does not exist, creating it now")
    # creating new file
    os.mknod("newfile.txt")
    # closing the file
    f.close

# if the file exists
if os.path.exists("nex-file.txt"): 
# print this message
    print("we are removing the file now which is nex-file.txt")
# remove the file
    os.remove("nex-file.txt")
    # closing the file
f.close()

# with and as statements 
# open a file using with and as statments
with open("names.txt") as f:
# add code to read the file and add inside newly created variable "content"
    content = f.read()
# print the content of the file
    print(content)