#01 -> Find area of recaangle 
'''
length = int(input("Enter the length of the rectangle "))
width = float(input("Enter the width of the rectangle "))

area = length * width;

print(f"The area of the retangle with lenght as {length} and width as {width} is {area}")


'''

#02 -> Shoppingcart Program 
'''

item = input("What Item would you like to buy? ");
price = float(input("What is the price?  "));
quantity = int(input("How many would you like ??  "))
Total = price * quantity;

print(f"you have bought {quantity} X {item}. ")
print (f"your total is {Total}. ");


'''




#03 -> Madlib Game
# Madlib is a word game where you fill in the blanks of a story with random words.

adjective1= input("Enter an adjective: (Describing word) ");
noun1= input("Enter a noun:(person, place or thing ) ");
adjective2= input("Enter an adjective: (Describing word) ");
verb1 = input("Enter a verb: (action word) ending with -ing ");
adjective3= input("Enter an adjective: (Describing word) ");

print(f"Today I went to the zoo. I saw a {adjective1} {noun1} jumping up and down in its tree. He {verb1} {adjective2} through the large tunnel that led to its {adjective3} {noun1}. ")

print(f"Today I went to a {adjective1} zoo");
print(f"In an exhibit i saw a {noun1}");
print(f"{noun1} was {verb1} {adjective2}");
print(f"i was {adjective3}");