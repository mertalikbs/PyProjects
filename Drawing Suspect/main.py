import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

universe_list = ["Star Wars", "Spiderman", "Harry Potter", "Grand Theft Auto", 
                 "Breaking Bad", "The Walking Dead", "The Simpsons", "Attack on Titan", 
                 "Demon Slayer", "One Piece", "Naruto", "Dragon Ball", "Jojo's Bizarre Adventure", 
                 "Death Note", "One Punch Man"]


numbers = []

def UniverseSelection():
    global random_universe
    random_universe = random.choice(universe_list)

def PlayerCount():
    playerNumber = int(input("How many player are you? "))
    clear_console()
    for i in range(playerNumber):
        numbers.append(i+1)

def Game():
    PlayerCount()
    imposter = int(random.choice(numbers))

    for _ in range(len(numbers)):
        number = int(input("What is your number? "))
        if number == imposter:
            print("You are the imposter")
            time.sleep(3) 
            clear_console()
        else:
            print(f"The universe is {random_universe}")
        time.sleep(3) 
        clear_console()
    
    print("Have a great game!")

def Main():
    UniverseSelection()
    Game()
    numbers.clear()

gameIsContinuing = True

while gameIsContinuing == True:
    Main()
    gameIsContinuing = (True if input("Would you want another game?\n y for Yes and n for No\n") == "y" 
                        else False)
    clear_console()