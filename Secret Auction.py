from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

# adların bulunduğu liste, ad ve teklif girilecek, temizlenecek, hayır denilene kadar devam edilecek, kazanan gösterilecek

print(logo)
persons = []
auction = True
winnerName = ""
winnerOffer = 0

while auction == True:
    name = input("What is your name?\n")
    offer = int(input("What is your offer for auction?\n$"))
    addingPerson = {
        "Name": name,
        "Offer": offer
    }
    if offer > winnerOffer:
        winnerName = name
        winnerOffer = offer
    persons.append(addingPerson)
    answer = input("Is there another player participant for offering? Type yes or no?")
    if answer == "yes":
        auction = True
        clear()
    elif answer == "no":
        auction = False
        clear()
        print(f"Auction has ended. The winner is {winnerName} with {winnerOffer}$.")
        print(logo)
    else:
        print("You've entered invalid command. The auction has ended.")
        auction = False