from art import logo
import random
print(logo)

def should_continue():
    answer = input("Do you want to play a game of Blackjack? Type 'y' for yes and 'n' for no.\n")
    if answer == "y":
        return True
    elif answer == "n":
        print("Thank you for playing Blackjack. Goodbye.")
        return False
    else:
        print("Your command is invalid. Game finished.")
        return False

def winner():
    your_total_score = userscore()
    computers_total_score = computerscore()
    if your_total_score == computers_total_score:
        return "Draw.😯"
    elif your_total_score > 21:
        return "You lost.😭"
    elif computers_total_score > 21:
        return "You won.😎"
    elif your_total_score > computers_total_score:
        return "You won.😎"
    elif computers_total_score > your_total_score:
        return "You lost.😭"

def userscore():
    your_total_score = 0
    for number in your_hand:
        your_total_score += number
    return your_total_score

def computerscore():
    computers_total_score = 0
    for number in computers_hand:
        computers_total_score += number
    return computers_total_score

def screen():
    your_total_score = userscore()
    computers_total_score = computerscore()
    print(f"    Your cards: {your_hand}, current score: {your_total_score}")
    print(f"    Computer's cards: {computers_hand}, computer's final score: {computers_total_score}")
    print(winner())

decision = should_continue()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_hand = [random.choice(cards), random.choice(cards)]
computers_hand = [random.choice(cards)]

while decision:
    your_total_score = userscore()
    computers_total_score = computerscore()
    print(f"    Your cards: {your_hand}, current score: {your_total_score}")
    print(f"    Computer's cards: {computers_hand}, computer's score: {computers_total_score}")
    answer = input("Type 'y' to get another card, type 'n' to pass.  ")
    if answer == "y":
        random_num = random.choice(cards)
        your_hand.append(random_num)
        if userscore() > 21 and 11 in your_hand:
            your_hand.remove(11)
            your_hand.append(1)
            if userscore() > 21:
                screen()
                decision = False
        elif userscore() > 21:
            screen()
            decision = False
    if answer == "n":
        while computerscore() < 17:
            random_num = random.choice(cards)
            computers_hand.append(random_num)
        if computerscore() > 21 and 11 in computers_hand:
            computers_hand.remove(11)
            computers_hand.append(1)
        screen()
        decision = False