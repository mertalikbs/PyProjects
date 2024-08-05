# Uygulama logoyla açılır. Compare A ve Against B yazıları çıkar.
# Kullanıcıdan seçim yapması istenir. Yüksek rakamlı kişiyi seçerse puan eklenir ve devam eder.
# Kullanıcı yanlış cevap verdiği takdirde oyun sonlanır ve oyuncunun puanı yazılarak kaybettiği ekrana verilir.

from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)

def game():
    score = 0
    isContinue = True
    while isContinue:
        p1 = random.choice(data)
        p2 = random.choice(data)
        print(f"Compare A: {p1['name']}, {p1['description']}, {p1['country']}.")
        print(vs)
        print(f"Against B: {p2['name']}, {p2['description']}, {p2['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B'.  ").title()
        A = p1['follower_count']
        B = p2['follower_count']
        if answer == "A":
            if A > B:
                score += 1
                clear()
                print(f"You're right. Current score: {score}")
            else:
                isContinue = False
                clear()
                print(f"Sorry, that's wrong. Final score: {score}")
        elif answer == "B":
            if B > A:
                score += 1
                clear()
                print(f"You're right. Current score: {score}")
            else:
                isContinue = False
                clear()
                print(f"Sorry, that's wrong. Final score: {score}")
        else:
            clear()
            print("Your command is invalid. Game over.")
            print(f"Final score: {score}")

game()