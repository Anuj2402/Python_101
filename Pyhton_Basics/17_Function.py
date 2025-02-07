# Function -> A block of reusable code 
# place () after the function name to invoke it 

# Function to print a birthday message
def happy_birthday(name, age):
    print(f"Happy birthday to you, {name}!")
    print(f"You are {age} years old!")

# Function to display an invoice
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# Invoking the functions
happy_birthday("Anuj", 22)
display_invoice("Anuj", 1000, "01/JAN")

print('-' * 50)

# Functions to perform basic arithmetic operations
def add_num(x, y):
    return x + y

def sub_num(x, y):
    return x - y

def mul_num(x, y):
    return x * y

def divide_num(x, y):
    return x / y

# Testing the arithmetic functions
print(add_num(2, 3))
print(sub_num(2, 3))
print(mul_num(2, 3))
print(divide_num(2, 3))

print('-' * 50)

# Function to create a full name with capitalized first and last names
def create_name(first, last):
    first = first.capitalize()  # Capitalize the first letter of the first name
    last = last.capitalize()    # Capitalize the first letter of the last name
    return first + " " + last

# Testing the create_name function
full_name = create_name("Anuj", "kumar")
print(full_name)
