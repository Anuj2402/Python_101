#nasted loops -> loop inside a loop
#.     outer loop 
#         inner loop 

rows = int(input("Enter the number of rows: "));
columns = int(input("Enter the number of columns: "));
symbol = input("Enter a symbol to use: ");

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ");
    print(); # -> This is used to print a newline
print("End of the program");

#example 2 -> print a triangle
rows = int(input("Enter the number of rows: "));
symbol = input("Enter a symbol to use: ");

for i in range(rows):
    print(symbol * (i+1));
print("End of the program");


