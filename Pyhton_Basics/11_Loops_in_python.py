# while loop -> while loop is used to execute a block of statements repeatedly until a given condition is satisfied.
# Syntax:
# while condition:
#     statement1
#     statement2
#     statement3
#     ....                      
# Example:
# i = 1;
# while i <= 10:    
#     print(i);
#     i = i + 1;

'''
name = input("Enter your name: ");

while name == "":
    print("Please enter your name");
    name = input("Enter your name: ");

print(f"Goodmorning {name}");
'''
'''
age = int(input("Enter your age: "));
while age<=0:
    print("Please enter a valid age");
    age = int(input("Enter your age: "));
print(f"Your age is {age}");
'''
'''
food = input("Enter your favourite food or (q to quit ) ");
while not food == "q":
    print(f"I like {food} too");
    food = input("Enter your favourite food or (q to quit ) ");
 '''  
#logical operators to while loop
# and, or, not
# and -> Returns True if both statements are true
# or -> Returns True if one of the statements is true
# not -> Reverse the result, returns False if the result is true
'''
num2 = int(input("Enter a number between 1 and 10 : "));
while num2 <1 or num2 >10:
    print("Please enter a valid number");
    num2 = int(input("Enter a number between 1 and 10 : "));
print(f"Your number is {num2}");
'''

#Python compount interest calculator
# A = P(1 + r/n)^(nt)
# A = the future value of the investment/loan, including interest
# P = the principal investment amount (the initial deposit or loan amount)
# r = the annual interest rate (decimal)
# n = the number of times that interest is compounded per year
# t = the number of years the money is invested/borrowed for
'''
pricipal =0;
rate = 0;
time = 0;

while pricipal<=0:
    pricipal = float(input("Enter the principal amount: "));
    if pricipal<=0:
        print("Please enter a valid principal amount pricipal amount should be greater than 0");

while rate<=0:
    rate = float(input("Enter the rate of interest : "));
    if rate<=0:
        print("Please enter a valid rate of interest rate of interest should be greater than 0");

while time<=0:
    time = float(input("Enter the time period in years : "));
    if time<=0:
        print("Please enter a valid time period time period should be greater than 0");

print(f"Principal amount : {pricipal}");
print(f"Rate of interest : {rate}");
print(f"Time period : {time}");

total = pricipal * (1 + rate/100)**time; #-> formula for compound interest
print(f"Balance after {time} years is RS{total:.2f}");
'''


print("For loop in pyrhon : "); 
# for loop -> for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Syntax:
# for variable in sequence:
#     statement1
#     statement2
#     statement3
#     ....
# Example:
# for i in range(1,11):
#     print(i);

'''
for i in range(1,11):
    print(i);
'''
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x);
