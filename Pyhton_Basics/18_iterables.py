'''
Iterables -> An object/collection that can return it's elements one at a time,
allowing it to be iterated over in a loop 

'''


numbers_list  = [1,2,3,4,5]
numbers_tuple = (1,2,3,4,5)
numbers_set = {1,2,3,4,5}
numbers_string = "12345"
for num in numbers_list:
    print(num, end=" "),

print("Printing the number list in reverse order ")
for num in reversed(numbers_list):
    print(num, end=" ")

print("\nPrinting the number tuple in reverse order ")
for num in reversed(numbers_tuple):
    print(num, end=" ")

print("\nPrinting the number set ")
for num in numbers_set:
    print(num, end=" ")
'''
print("\nPrinting the number set in reverse order ")
for num in reversed(numbers_set):
    print(num, end=" ")          # Set is unordered so it will not print in reverse order TypeError: 'set' object is not reversible
'''
print("\nPrinting the number string ")
for num in numbers_string:
    print(num, end=" ")

print("Now we will iterating over disctionary")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Printing the keys of dictionary")
for key in person:
    print(key, end="\n") # By default it will print the keys of dictionary
print("Printing the values of dictionary")
for value in person.values():
    print(value, end="\n") # By default it will print the values of dictionary
print("Printing the items of dictionary")

for key, value in person.items():
    print(key, value, end="\n") # By default it will print the items of dictionary

'''
Memebership operators in python -> in, not in -> used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary)
                                1. in 
                                2. not in 


'''

word = "APPLE"
student_set = {"John", "Jennie", "Jim", "Jack", "Joe"}

student = input("Enter the name of student: ")
 
if student in student_set:
    print(f"Yes, {student} is in the student set")
else:
    print(f"No, {student} is not in the student set")



letter= input("Guess a letter in the secret word: ")

if letter in word:
    print(f"Yes, the {letter} is in the word")
else:
    print(f"No, the {letter} is not in the word")