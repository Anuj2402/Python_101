friends = 5;


# Addition
#friends = friends + 1;
#friends += 1; # This is the same as above

# Subtraction
'''
friends = friends - 1;
friends -= 1; # This is the same as above
'''

# Multiplication
'''
friends = friends * 2;
friends *= 2; # This is the same as above
'''

# Division
'''
friends = friends / 2;
friends /= 2; # This is the same as above
'''

# Modulus -> Gives the remainder
'''
friends = friends % 2;
friends %= 2; # This is the same as above
'''

# Exponent -> Power
'''
friends = friends ** 2;
friends **= 2; # This is the same as above
'''


print(friends);

#Math related built in functions

X=3.14;
y=-4;
z=5;
result = round(X); # Rounds the number to the nearest whole number
result2 = abs(y); # Returns the absolute value of the number
result3 = pow(z,2); # Returns the power of the number
result4 = max(4,5); # Returns the maximum value of the two numbers
result5 = min(4,5); # Returns the minimum value of the two numbers
print("The roundup value of X is ",result);  # 3
print("The absolute value of y is ",result2); # 4
print("The power of z is ",result3); # 25
print("The maximum value of 4 and 5 is ",result4); # 5
print("The minimum value of 4 and 5 is ",result5); # 4


import math;

result6 = math.sqrt(25); # Returns the square root of the number
print("The square root of 25 is ",result6); # 5.0

result7 = math.ceil(3.7); # Returns the smallest integer greater than or equal to the number
print("The ceil value of 3.7 is ",result7); # 4

result8 = math.floor(3.7); # Returns the largest integer less than or equal to the number
print("The floor value of 3.7 is ",result8); # 3

result9 = math.pi; # Returns the value of pi
print("The value of pi is ",result9); # 3.141592653589793

result10 = math.e; # Returns the value of e
print("The value of e is ",result10); # 2.718281828459045

result11 = math.inf; # Returns the value of infinity
print("The value of infinity is ",result11); # inf

#Exercises01-> find the circumference of a circle
'''
radius = float(input("Enter the radius of the circle "));
circumference = 2 * math.pi * radius;
print(f"The circumference of the circle with radius as {radius} is {round(circumference)}");
'''

#Exercises02-> find the area of a circle
'''
radius = float(input("Enter the radius of the circle "));
area = math.pi * math.pow(radius,2);   
print(f"The area of the circle with radius as {radius} is {round(area)}");
'''
#Exercises03-> calculate the Hypotenuse of a right angled triangle
# Hypotenuse is the longest side of a right-angled triangle, the side opposite the right angle.
# The square of the hypotenuse is equal to the sum of the squares of the other two sides.
# a^2 + b^2 = c^2
# c = sqrt(a^2 + b^2)
# c = sqrt(3^2 + 4^2)
# c = sqrt(9 + 16)
# c = sqrt(25)
# c = 5
#So the hypotenuse of a right angled triangle with sides 3 and 4 is 5
'''
side1 = float(input("Enter the first side of the triangle "));
side2 = float(input("Enter the second side of the triangle "));
hypotenuse =math.sqrt(math.pow(side1,2) + math.pow(side2,2));
print(f"The hypotenuse of the right angled triangle with sides {side1} and {side2} is {round(hypotenuse)}");
'''

