#String Methods -> is a function that performs an operation on a string and returns the result.
#                -> Syntax -> string.method()
#                -> Example -> "Hello".upper() -> "HELLO"
#                -> Example -> "Hello".lower() -> "hello"
#                -> Example -> "Hello".title() -> "Hello"

name = input("Enter your name ");
print(name.upper()); #Change the string to uppercase
print(name.lower()); #Change the string to lowercase
print(name.title()); #Change the string to title case
print(name.capitalize()); #Change the string to capitalize case
print(name.swapcase()); #Change the string to swapcase case -> Lowercase to Uppercase and Uppercase to Lowercase
print(name.replace("a","e")); #replace the character in the string
print(name.find("a")); #Find the index of the character in the string
print(name.rfind("a")); #Find the index of the character in the string from the right   
print(name.isdigit()); #Check if the string is a digit
print(name.isalpha()); #Check if the string is an alphabet
print(name.isalnum()); #Check if the string is an alphanumeric
print(name.isspace()); #Check if the string is a space

#print(help(str)); #Get the help of the string methods

#Validate User Input Exercise
'''
1. username is not more than 12 characters
2. username must not contain spaces
3. username must not conatain degits
'''
username = input("Enter your username: ");

if len(username)>12:
    print("Username can not be more than 12 characters");
elif " " in username:
    print("Username can not contain spaces");
elif not username.isalpha():
    print("Username can not contain digits");
else:
    print(f"welcome {username}");
