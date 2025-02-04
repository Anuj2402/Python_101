#collection = single , "variable" used to store multiple values 
#list -> ordered, changeable, allows duplicate values
#tuple -> ordered, unchangeable, allows duplicate values, FASTER 
#set -> unordered, unindexed, NO duplicate values. but ADDING elements is faster and REMOVING elements is faster


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"];
print(fruits);
print(fruits[1]); # -> This will print the second element of the list
print(fruits[-1]); # -> This will print the last element of the list
print(fruits[2:5]); # -> This will print the elements from index 2 to index 4
print(fruits[:4]); # -> This will print the elements from index 0 to index 3
print("apple" in fruits); # -> This will check if the element is present in the list or not
print(len(fruits)); # -> This will print the length of the list
fruits.append("grapes"); # -> This will add the element to the end of the list
# print(help(fruits)); # -> This will print the help for the list
fruits.remove("banana"); # -> This will remove the element from the list
print(fruits);
fruits.pop(); # -> This will remove the last element from the list
print(fruits);


#Tuple
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
#Tuple items are ordered, unchangeable, and allow duplicate values.
example_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango");
print(example_tuple);
print(example_tuple[1]); # -> This will print the second element of the tuple
print(example_tuple[-1]); # -> This will print the last element of the tuple
print(example_tuple[2:5]); # -> This will print the elements from index 2 to index 4
print(example_tuple[:4]); # -> This will print the elements from index 0 to index 3
print("apple" in example_tuple); # -> This will check if the element is present in the tuple or not
print(len(example_tuple)); # -> This will print the length of the tuple
# print(help(example_tuple)); # -> This will print the help for the tuple
#example_tuple.append("grapes"); # -> This will add the element to the end of the tuple
#example_tuple.remove("banana"); # -> This will remove the element from the tuple
#example_tuple.pop(); # -> This will remove the last element from the tuple
#example_tuple[1] = "mango"; # -> This will give an error because tuples are unchangeable
#del example_tuple; # -> This will delete the tuple
print(example_tuple);

for x in example_tuple:
    print(x);
for fruit in fruits:
    print(fruit);



#Set
#Sets are used to store multiple items in a single variable.
#A set is a collection which is both unordered and unindexed.
#Sets are written with curly brackets.
#Set items are unordered, unchangeable, and do not allow duplicate values.
example_set = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"};
print(example_set);
print("apple" in example_set); # -> This will check if the element is present in the set or not
example_set.add("grapes"); # -> This will add the element to the set
print(example_set);
example_set.update(["grapes", "papaya", "watermelon"]); # -> This will add multiple elements to the set 
print(example_set);
example_set.remove("banana"); # -> This will remove the element from the set    
print(example_set);
example_set.discard("banana"); # -> This will remove the element from the set
print(example_set);
example_set.pop(); # -> This will remove the last element from the set
print(example_set);
example_set.clear(); # -> This will clear the set
print(example_set);
del example_set; # -> This will delete the set
#print(example_set); # -> This will give an error because the set is deleted

#Exercise-> Shopping cart program
#Create a shopping cart program that takes the input from the user and adds the items to the cart

foods = [];
prices = [];
total = 0;

while True:
    food_item = input("Enter the food item:(q to quit) "); 
    if food_item.lower() == "q":
        break;
    else:
        Price = float(input("Enter the price: "));
        foods.append(food_item); #-> This will add the food item to the list
        prices.append(Price); #-> This will add the price to the list
        total += float(Price); #-> This will add the price to the total


print("-------------Your Cart-----------------");

for food in foods:
    print(food, end = " ")

print("\nyouTotal: ", total);


print('*' * 60);



# 2D List -> A list inside a list
# A 2D list is a list that contains other lists.
# A 2D list is a list that contains one or more lists.
'''
fruits = ["apple", "banana", "cherry", "orange", "Kiwi" ];
vegetables = ["carrot", "tomato", "potato", "onion", "cucumber"];
meats = ["chicken", "beef", "mutton", "fish", "pork"];
grocery = [fruits, vegetables, meats];
print("Printing the list inside list i.e 2D List", grocery);
print("Printing the first index of grocery which is a list indie a list ", grocery[0]); # -> This will print the first list
print(grocery[1]); # -> This will print the second list
print(grocery[2]); # -> This will print the third list
print(grocery[0][1]); # -> This will print the second element of the first list
print(grocery[1][2]); # -> This will print the third element of the second list

grocery2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
print(grocery2); # -> This will print the list inside the list
print(grocery2[0]); # -> This will print the first list
print(grocery2[1]); # -> This will print the second list
print(grocery2[2]); # -> This will print the third list
print(grocery2[0][1]); # -> This will print the second element of the first list
print(grocery2[1][2]); # -> This will print the third element of the second list
print(grocery2[2][0]); # -> This will print the first element of the third list
'''

print('*'"2D Tuple" * 60);
'''
#2D Tuple
#A 2D tuple is a tuple that contains other tuples.
#A 2D tuple is a tuple that contains one or more tuples.

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9));
print(num_pad); # -> This will print the tuple inside the tuple

#Printing the 2D tuple
for row in num_pad:
    for num in row:
        print(num, end = " ");
    print(); # -> This will print the new line after each row
'''

print("____________PYTHON QUIZ GAME _____________");

#Quiz Game
#Create a quiz game that asks the user questions and gives the user the score at the end of the quiz

questions = ("How many elements are in the periodic table?",
                "which animal lays the largest eggs?:", 
                "what is the most abundant gas in the earth's atmosphere?",
                 "How many bones are in the human body?",
                  "which planet in the solar system is the hottest?");

options = (("A. 118", "B. 120", "C. 119", "D. 121"),
                 ("A. Ostrich", "B. Kiwi", "C. Emu", "D. Penguin"),
                  ("A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 208", "C. 210", "D. 212"),
                    ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
                    ("A. 118", "B. 120", "C. 119", "D. 121"))

answers = ("A", "A", "A", "A", "A"); # -> This will store the answers of the questions
guesses = []; # -> This will store the guesses of the user
score = 0; # -> This will store the score of the user
question_num = 0; # -> This will store the question number

for question in questions:
    print("-------------------------------------");
    print(question);
    for option in options[question_num]:
        print(option);
    guess = input("Enter the answer: (A , B, C ,D) ").upper();
    guesses.append(guess);
    if guess == answers[question_num]:
        score += 1;
        print("Correct");
    else:
        print("Incorrect");
        print(f"The correct answer is {answers[question_num]}");

    question_num += 1; # -> This will increment the question number

for answer in answers:
    print(answer , end = " ");
print();
for guess in guesses:
    print(guess, end = " ");
print();


print(f"Your score is {score} out of {len(questions)} and your percentage is {score/len(questions) * 100}%");
