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
print(help(fruits)); # -> This will print the help for the list
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
print(help(example_tuple)); # -> This will print the help for the tuple
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

