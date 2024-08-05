
#HINT: You can call clear() to clear the output in the console.


# adların bulunduğu liste, ad ve teklif girilecek, temizlenecek, hayır denilene kadar devam edilecek, kazanan gösterilecek

persons = {}
auction = True

while auction == True:
    name = input("What is your name?\n")
    offer = int(input("What is your offer for auction?\n$"))
    addingPerson = {
        name: offer
    }
    persons.update(addingPerson)
    # Bir dict'e başka bir dict eklemek için kullanılabilir.
    answer = input("Is there another player participant for offering? Type yes or no?")
    if answer == "yes":
        auction = True
    elif answer == "no":
        auction = False
        maxName = max(persons, key=persons.get)
        # max(liste adı, key=liste adı.get) sayesinde değeri en yüksek olan KEYi dict'den çıkardık.
        maxOffer = max(persons.values())
        # max(dict.values()) fonksiyonu en yüksek sayıyı verecektir.
        print(f"The secret auction over. Our winner is {maxName} with {maxOffer}$ offering! Congratulations {maxName}!")
        for person in persons:
            offer = persons[person]
            print(f"{person}: {offer}")
    else:
        print("You've entered invalid command. The auction has ended.")
        auction = False