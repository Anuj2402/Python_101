'''
List comprehension is a concise way to create lists.
 It consists of brackets containing an expression followed by a for clause,
   then zero or more for or if clauses. 
   The expressions can be anything, meaning you can put in all kinds of objects in lists.
  
   [expression for value in iterable if condition]


'''
# List comprehension with strings
print("List comprehension with strings")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [fruit for fruit in fruits if "a" in fruit]
print(fruits_with_a)
fruits_first_letter = [fruit[0] for fruit in fruits]
print(fruits_first_letter)
print("List comprehension with numbers")
# List comprehension with numbers
numbers = [1, -2, 3, -4, 5, 6, -7, 8, 9]
squared_numbers = [number**2 for number in numbers]
print("The required square numbers are ",squared_numbers)
positive_numbers = [number for number in numbers if number > 0]
print("The required posistive numbers are ",positive_numbers)
negative_numbers = [number for number in numbers if number < 0]
print("The required negative number are",negative_numbers)
even_numbers = [number for number in numbers if number % 2 == 0]
print("The required even number are  ",even_numbers)
odd_numbers = [number for number in numbers if number % 2 != 0]
print("The required odd number are ",odd_numbers)
