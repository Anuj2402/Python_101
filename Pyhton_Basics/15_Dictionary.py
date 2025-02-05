#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#In Python dictionaries are written with curly brackets, and they have keys and values.

#Dictionary
#Dictionaries are used to store data values in key:value pairs.

capitals = { "India" : "New Delhi", 
            "USA" : "Washington DC", 
            "UK" : "London",
              "France" : "Paris", 
              "Germany" : "Berlin"};
print(capitals);
print(capitals["India"]); # -> This will print the value of the key "India"
print(capitals.get("USA")); # -> This will print the value of the key "USA"
print(capitals.get("japan")); # -> This will print None because the key is not present in the dictionary
capitals["India"] = "Delhi"; # -> This will change the value of the key "India"
print(capitals);
for x in capitals:
    print(x); # -> This will print the keys of the dictionary
for x in capitals:
    print(capitals[x]); # -> This will print the values of the dictionary
for x in capitals.values():
    print(x); # -> This will print the values of the dictionary

if capitals.get("India") == "Delhi":
    print("Yes, the value is Delhi");
else:
    print("No, the value is not Delhi");

capitals.update({"India" : "New Delhi"}); # -> This will update the value of the key "India"
print(capitals);
capitals["Japan"] = "Tokyo"; # -> This will add a new key value pair to the dictionary
print(capitals);
capitals.pop("Japan"); # -> This will remove the key value pair from the dictionary
print(capitals);
capitals.popitem(); # -> This will remove the last key value pair from the dictionary

# capitals.clear(); # -> This will clear the dictionary

keys = capitals.keys(); # -> This will return the keys of the dictionary

for key in capitals.keys():
    print("The keys is ", key);

values = capitals.values(); # -> This will return the values of the dictionary

for value in capitals.values():
    print("The values is ", value);

items = capitals.items(); # -> This will return the key value pairs of the dictionary

for key, value in capitals.items():
    print(f"{key} : {value}");


#Nested Dictionary
#A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
    }
print(myfamily); # -> This will print the nested dictionary
print(myfamily["child1"]); # -> This will print the nested dictionary of child1
print(myfamily["child1"]["name"]); # -> This will print the name of child1
print(myfamily["child1"]["year"]); # -> This will print the year of child1
print(myfamily.get("child2")); # -> This will print the nested dictionary of child2
print(myfamily.get("child2").get("name")); # -> This will print the name of child2
print(myfamily.get("child2").get("year")); # -> This will print the year of child2
print(myfamily.get("child3")); # -> This will print the nested dictionary of child3
print(myfamily.get("child3").get("name")); # -> This will print the name of child3

#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.

#Method	Description
#clear()	Removes all the elements from the dictionary
#copy()	Returns a copy of the dictionary
#fromkeys()	Returns a dictionary with the specified keys and values
#get()	Returns the value of the specified key
#items()	Returns a list containing a tuple for each key value pair
#keys()	Returns a list containing the dictionary's keys
#pop()	Removes the element with the specified key


print('-' * 50)

# concession stand program 

menu = {"pizza": 3.00,
         "nachos": 4.50,
         "popcorn": 6.00,
         "fries": 2.50,
         "chips": 1.00,
         "pretzel": 3.50,
         "soda" : 3.00,
         "lemonade": 4.25}

cart = []; # -> This is a list that will store the food iteams 
total = 0;

print("___________________MENU______________________")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("---------------------------------------")

while True:
    food = input("select an item (q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart) 
print("_____________YOUR ORDER________________________________")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()

print(f"your total is ${total:.2f}")
