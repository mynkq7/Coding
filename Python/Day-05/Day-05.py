# While loops = execute some code while a condition is true 
# Asking user for name
name = input("Enter your name:") 
# If the name is empty
while name == "": 
 # Print this message
    print("you did not enter your name")
# Ask for the name again
    name = input("Enter your name:") 
 # If the ccondition is false, we exit the loop and print the name
print(f"Hello {name}")

# Asking users for age
age = int(input("Enter your age:")) 
# While age is less than 0
while age <0: 
# Print this message    
    print("The age cannot be negative") 
# Ask for the user input again 
    age = int(input("Enter your age:")) 
# If the confition is false, we exit the loop and print the age 
print(f"you are {age} years old")

# Asking users to enter their favorite food c  num = int(input("Enter a number between 1 and 10:"))

food = input("Enter your favourite food (press 'q) to quit:")
# While the food is not equal to q
while not food == 'q': 
# Print this message
    print(f"your favourite food is {food}") 
# Askingusers to enter food again
    food = input("Enter your favourite food again (press 'q) to quit:")
# If the condition is false, we exit the loop and print the message 
print("you have exited the loop")

# Asking users to enter a number that is between 1 and 10 
num = int(input("Enter a number between 1 and 10:"))
# While the number is less than 1 or greater than 10
while num < 1 or num > 10: 
# Print this message
   print("The entered number is invalid")
#    Asking users to enter the number between 1 and 10 again
   num = int(input("Enter a number between 1 and 10:"))
# If the condition is false, we exit the loop and print the number 
print(f"your entered number is {num}")  

# Funtions
# Defining a function to say happy birthday which is happy_birthday
def happy_birthday(name, age):
# Printing the birthday messages
    print(f"happy birthday to you")
    print(f"happy birthday to you")
    print(f"happy birthday dear {name}")
    print(f"happy birthday to you")
    print(f"You are now {age} years old!")
 # Calling the function
happy_birthday("Alice","21")

# Defining a function to generate inovice which is generate_invoice
def generate_invoice(Customer_name, amount, date):
 # Printing the invoice details
     print(f"Hello {Customer_name}")
     print(f"Your invoice amout is ${amount}")
     print(f"The due date is on {date}")
 #  Calling the function
generate_invoice("bob", "240", 202409-30)

# Retrun statement
# Defining a function to calculate the two numbers named add
def add(x,y):
# Adding the two number x and y
   z = x+y
# Retruing the result to z variable
   return z 

# Defining a functon to subtract the two numbers named sub
def sub(x,y):
 # Subtracting two numbers x and 
    z = x-y
 # Returning the results to z variable
    return z 

# Defining a function to multiply the two numbers named mul
def mul(x,y):
# Multiplying the two numbers x and y
    z = x*y
#    Returing the results to z variable
    return z 

# Defining a function to divide the two numbers named div 
def div(x,y):
 # Diving the two numbers x and y
    z = x/y
# Returning the results to z variable
    return z
# Printing the results of the functions 
print(add(10,5))
print(sub(10,5))
print(mul(10,5))
print(div(10,5))

# Defining a function with name create_name 
def create_name (first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    full_name = f"{first_name} {last_name}"
    return full_name
# Printing the results of the function create_name 
print(create_name("mayank","naithani"))
