from replit import clear

game_table = [["◼", "◼", "◼"], ["◼", "◼", "◼"], ["◼", "◼", "◼"]]

player1 = input("What's the name of player 1?\n")
player2 = input("What's the name of player 2?\n")
clear()

game_ended = False
while not game_ended:
    choice = input(f"Write your choice in order row and column {player1}. Example: To select first row and second column write 12.\n")
    row = int(choice[0]) - 1
    column = int(choice[1]) - 1
    game_table[row][column] = "X"
    for x, y, z in game_table:
        print(x, y, z)
    choice2 = input(f"Write your choice in order row and column {player2}.\n")
    clear()
    row2 = int(choice2[0]) - 1
    column2 = int(choice2[1]) - 1
    game_table[row2][column2] = "O"
    for x, y, z in game_table:
        print(x, y, z)
    