# Task 1 Random Choice Game

import random

list_of_items = ["ball", "bat", "helmet", "gloves"]
item_chosen = random.choice(list_of_items)
user_guess = input("What is the item that was randomly selected? (ball, bat, helmet, or gloves): ")

if item_chosen == user_guess:
    print(f"Great job! The item chosen was {item_chosen}.")
else:
    print(f"Better luck next time! You incorrectly guessed {user_guess} when {item_chosen} was actually selected.")

'''
This program works by importiung the random package, creating the list of items that could possible be chosen
then choosing from that list by assigning the random choice to the item chosen variable and then using
the input function to take the user's guess. It is followed by an if-else conditional that compares
the actual chosen item to the user's guess and then uses an f-string print statement to tell the user
if they guessed correctly or incorrectly while revealing the actual result.
'''