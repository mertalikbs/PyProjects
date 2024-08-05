
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lowed = name1.lower()
name2_lowed = name2.lower()

count_true1 = name1_lowed.count("t") + name1_lowed.count("r") + name1_lowed.count("u") + name1_lowed.count("e")
count_true2 = name2_lowed.count("t") + name2_lowed.count("r") + name2_lowed.count("u") + name2_lowed.count("e")
true_total = count_true1 + count_true2

count_love1 = name1_lowed.count("l") + name1_lowed.count("o") + name1_lowed.count("v") + name1_lowed.count("e")
count_love2 = name2_lowed.count("l") + name2_lowed.count("o") + name2_lowed.count("v") + name2_lowed.count("e")
love_total = count_love1 + count_love2

score = str(true_total) + str(love_total)
score_int = int(score)

if score_int <=10 or score_int >=90:
    #or koyman gerekirdi çünkü bir aralık değil iki aralık var.
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score_int <=50 and score_int >=40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")