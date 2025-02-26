'''
Match case statement is a new feature in Python 3.10. It is similar to switch case statement in other programming languages.
It is used to compare the value of a variable to multiple values.
execute some code if a value matches a "case" value.
The match case statement is written using the match keyword.


'''

# Example 1
print("Example 1")
fruit = "apple"
match fruit:
    case "apple":
        print("Apple is my favorite fruit")
    case "banana":
        print("Banana is my favorite fruit")
    case "cherry":
        print("Cherry is my favorite fruit")
    case "kiwi":
        print("Kiwi is my favorite fruit")
    case "mango":
        print("Mango is my favorite fruit")
    case _:
        print("I don't like any other fruit")

# Example 2
print("Example 2")
def day_of_week(day):
    match day:
        case "Monday":
            print("Today is Monday")
        case "Tuesday":
            print("Today is Tuesday")
        case "Wednesday":
            print("Today is Wednesday")
        case "Thursday":
            print("Today is Thursday")
        case "Friday":
            print("Today is Friday")
        case "Saturday":
            print("Today is Saturday")
        case "Sunday":
            print("Today is Sunday")
        case _:
            print("Invalid day")
day_of_week("Monday")
day_of_week("Tuesday")
