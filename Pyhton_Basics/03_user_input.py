'''
Input()-> A function that prompts the user to  enter Data , it always returns the enter data as string 

so if the enter data is integet we should always typecast it as it will come as string initially 
'''

name = input("What is your name please type it here..");
age = int(input("what is your age ")); # int used here to type cast the string value in integer 

print(f"Hello mr {name}");
print("HAPPY BIRTHDAY !!!")
age = age + 1; 
print(f"you are now {age}. years old")