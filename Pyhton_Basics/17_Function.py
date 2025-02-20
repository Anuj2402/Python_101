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
# return = statement used to end a function and send a result back to the caller 

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
full_name = create_name("Anuj", "kumar") # storing the result in the full name varable 
print(full_name)


'''
Default arguments In the Function -> A default value for a certain parameters default is used when that arguments is 
omitted make your function more flexible , reduce # of arguments 
1. positional , 2. DEFAULT, 3. keyword , 4. Arbitrary 

'''
print("Default Arguments  Function Examples")
def net_price(list_price, discount=0 , tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500 , 0.1)) # oif argument is passed over the default argument then the default argument will be overwrite 


#EXERCISE 

import time 

def count(end , start =0):  #default argument should after any positional argument 
    for x in range(start , end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(0,10) 
# count(10)

print("KEYWORD ARGUMENTS ")
'''
KeyWord Arguments = An arguments preceded by an identifier, helps with readability, order of argumennts doesn't matter 
1. POSITIONAL  2. DEFAULT, 3. keyword , 4. Arbitrary
'''

def hello(greeting , title , first , last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", title = "Mr" , first = "Spongebob" , last = "Squarepants")

def get_phone(country ,  area , first , last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first= 456, last=7890)

print("Your phone number is ", phone_num)

# ARBITRARY Argumenst 
print(" ARBITARARY ARGUMENTS ")

'''
ARBITARARY Argiments Contains both Non keryword argumensts called as (args) and keyWord Arguments knowm as Kwargs

*args = allows you to pass multiple non-key argumnets 
**kwargs = allows you to pass multiple keywords- arguments 
  -> "*" unpacking operators 
 1. positional 2. default 3 . keywords  4. ARBITARARY 

'''

# *args will convert the passed parameters into the Tupple args name can vari we can give any name that we like 
print("*args OutPUT ")
def add( *args):
    print(type(args)) # It Output as TUPLE 
    total = 0
    # it will iterate over as it is converted into tules 
    for arg in args: 
        total += arg
    return total;

# suppose name has so many parameters like firt , middle , and last name 
def display_name1(*args):
    for arg in args:
        print(arg , end= " ")
print(add(1,2,3, 5))
display_name1("Dr.", "Spongebob" , "Harold ", "Squarepants", "III")
display_name1("\n")

print ("**kwargs  OUTOUT ")

def print_address(**kwargs):
    print(type(kwargs)) # it will print as dict 
    for  key, value in kwargs.items():
        print(f"{key}: {value}")
print_address(street = "123 fake St.",
                city = "Detroit ",
                state = "MI",
                zip = "54321"
                )

# *argsg and Kwargs in one funtion here oder will matter 
def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs:
    # print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}{kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
                    street = "123 fake St.",
                city = "Detroit ",
                apt = "#100",
                state = "MI",
                zip = "54321"
                            )




