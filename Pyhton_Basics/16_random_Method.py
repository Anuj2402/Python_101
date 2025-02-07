#random-> The random module in Python provides functions for generating random numbers, s
# electing random elements, and performing random operations

'''
To Know more about the random method of python use 
print(help(random))

'''

import random 

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5","6","7","8","9","10","J","Q","K","A"]
#number = random.randint(1,20)
# number = random.randint(low , high)
number = random.random()
option = random.choice(options)

random.shuffle(cards) # this will shuffel the cards on every iteration 
print(cards)
print("This is yout option", options)
print(number) 

print('-' * 50)
'''
#Python number guessing game 
# import random is already done in this file 

lowest_num =1
highest_num = 100

answer = random.randint(lowest_num , highest_num)
# print(answer)
guesses =0
is_running = True

print("Pyhton Number Guessing game ")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    try:
        guess = int(input(f"Guess a number between {lowest_num} and {highest_num}: "))
        if guess < lowest_num or guess > highest_num:
            print(f"Please enter a number within the range {lowest_num} to {highest_num}.")
            continue
        guesses += 1
        
        if guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {answer} in {guesses} tries.")
            is_running = False
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("Thanks for playing!")
'''
print('-' * 50)

# ROCK PAPER SCISSORS GAME 
print("---ROCK----PAPER----SCISSORS---GAME----")

options2 = ("rock", "paper", "scissors")
play_again = "yes"

while play_again.lower() == "yes":
    player = None
    computer = random.choice(options2)

    while player not in options2:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")


