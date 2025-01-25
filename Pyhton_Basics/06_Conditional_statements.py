# IF -> Do soemthing if a condition is met
# ELSE -> Do something else if the condition is not met
# ELIF -> Do something else if the first condition is not met
#      and the second condition is met          

#Exercises01-> Based on the age of the user, print the category of the user
'''
age= int(input("Enter your age "));
if age >= 100:
    print("You are a centenarian");
elif age >= 18:
    print("You are an adult");
elif age >= 13:
    print("You are a teenager");
else:
    print("You are a minor");
'''

#Exercises02-> print even or odd based on the number entered by the user
'''
number = int(input("Enter a number "));
if number % 2 == 0:
    print("The number is even");    
else:
    print("The number is odd");
'''
#Exercises03-> print the grade based on the marks entered by the user
'''
marks = int(input("Enter the marks "));
if marks >=90:
    priint("The grade is A+");
elif marks >=80:
    print("The grade is A");
elif marks >=70:
    print("The grade is B+");
elif marks >=60:
    print("The grade is B");
elif marks >=50:
    print("The grade is C");
else:
    print("The grade is D");
'''

for_sale = True;
#Agar item for sale hai toh print karo "The item is for sale"
if for_sale:
    print("The item is for sale");
else:
    #Agar item for sale nahi hai toh print karo "The item is not for sale"
    print("The item is not for sale");

#Exercises04-> Python Calculator
'''
operation = input("Enter the operation you want to perform like (+,-,*,/) ");
number1 = float(input("Enter the first number "));
number2 = float(input("Enter the second number "));
if operation == "+":
    print(f"The sum of {number1} and {number2} is {number1 + number2}");
elif operation == "-":
    print(f"The difference of {number1} and {number2} is {number1 - number2}");
elif operation == "*":
    print(f"The product of {number1} and {number2} is {number1 * number2}");
elif operation == "/":
    print(f"The division of {number1} and {number2} is {number1 / number2}");
else:
    print("Invalid operation");
'''

#Exercises05-> Python Weight Converter
'''
weight = float(input("Enter the weight "));
unit = input("Enter the unit of the weight ");
if unit == "kg":
    print(f"The weight in pounds is {weight * 2.20462}");
elif unit == "lbs":
    print(f"The weight in kilograms is {weight / 2.20462}");
else:
    print(f"{unit}. is Invalid unit");
'''



#Ternaary Operator -> A single line if else statement 
#                  -> Syntax -> variable = value1 if condition else value2
#                 -> If the condition is True, the value1 is assigned to the variable else value2 is assigned to the variable
#                -> Example -> result = "Pass" if marks >= 50 else "Fail"
#              -> Example -> print("The number is even") if number % 2 == 0 else print("The number is odd")


#example -> ternary operator to check if the number is even or odd
'''
number = int(input("Enter a number "));
result = "The number is even" if number % 2 == 0 else "The number is odd";
print(result);
'''
