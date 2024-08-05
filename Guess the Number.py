#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
 .d8888b.                                           888    888                    888b    888                        888                       
d88P  Y88b                                          888    888                    8888b   888                        888                       
888    888                                          888    888                    88888b  888                        888                       
888        888  888  .d88b.  .d8888b  .d8888b       888888 88888b.   .d88b.       888Y88b 888 888  888 88888b.d88b.  88888b.   .d88b.  888d888 
888  88888 888  888 d8P  Y8b 88K      88K           888    888 "88b d8P  Y8b      888 Y88b888 888  888 888 "888 "88b 888 "88b d8P  Y8b 888P"   
888    888 888  888 88888888 "Y8888b. "Y8888b.      888    888  888 88888888      888  Y88888 888  888 888  888  888 888  888 88888888 888     
Y88b  d88P Y88b 888 Y8b.          X88      X88      Y88b.  888  888 Y8b.          888   Y8888 Y88b 888 888  888  888 888 d88P Y8b.     888     
 "Y8888P88  "Y88888  "Y8888   88888P'  88888P'       "Y888 888  888  "Y8888       888    Y888  "Y88888 888  888  888 88888P"   "Y8888  888     
"""


import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard':  ")
number = random.randint(1, 101)

def live_mechanism(lives):
    while lives > 0:
        guess = int(input(f"    You have {lives} attempts remaining to guess the number.\n    Make guess:  "))
        if guess > number:
            print("It's high.")
            lives -= 1
        if guess < number:
            print("It's low.")
            lives -= 1
        if guess == number:
            print("You knew the number. Congratulations!")
            lives = -1
        if lives == 0:
            print(f"You have run out of guesses, you lose.\n  The number was {number}.")

def game(choice, number):
    global lives
    if choice == "hard":
        lives = 5
        live_mechanism(lives)
    if choice == "easy":
        lives = 10
        live_mechanism(lives)

game(choice, number)