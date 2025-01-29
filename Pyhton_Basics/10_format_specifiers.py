# format specifiers in python are used to format the output of the program in a specific way.
# format specifiers are used with the % operator.
#{value:flags} -> value -> the value to be formatted, flags -> optional, used to specify the formatting of the value.

#.(number)f -> number -> number of decimal places to be displayed. round the number to the specified decimal places.
#.(number)e -> number -> number of decimal places to be displayed in scientific notation. round the number to the specified decimal places.
#.(number)g -> number -> number of significant digits to be displayed. round the number to the specified significant digits.
# :03 = allocate zero padding to the left of the number
# :^ = center the value
# :< = left align the value
# :> = right align the value
# :+ = display the sign of the number
# :space = display the space of the number
# :_ = display the underscore of the number
# :, = display the comma of the number
# :b = display the binary of the number

#Example
price1 = 3.14159;
prince2 = 987.65;
price3 = 12.34;



print(f"Price 1 is ${price1}"); #Price1: 3.14
print(f"Price 1 is ${price1:.2f}"); #Price1: 3.14
print(f"Price 2 is ${price1}"); #Price2: 987.65
print(f"Price 2 is ${price1:.2f}"); #Price2: 987.65
print(f"price 3 is ${price3}"); #Price3: 12.34
print(f"price1 is ${price1:10}") #Price1: 3.14159 -> right align the value
print(f"price1 is ${price1:<10}") #Price1: 3.14159 -> left align the value
print(f"price1 is ${price1:^10}") #Price1: 3.14159 -> center the value
print(f"price1 is ${price1:+}") #Price1: +3.14159 -> display the sign of the number

