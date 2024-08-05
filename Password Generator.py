#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []

letters_selected = 0
for letter in letters:
  if letters_selected < nr_letters:
    letters_selected += 1
    chosen_letter = random.choice(letters)
    password.append(chosen_letter)

symbols_selected = 0
for symbol in symbols:
  if symbols_selected < nr_symbols:
    symbols_selected += 1
    chosen_symbol = random.choice(symbols)
    password.append(chosen_symbol)

numbers_selected = 0
for number in numbers:
  if numbers_selected < nr_numbers:
    numbers_selected += 1
    chosen_number = random.choice(numbers)
    password.append(chosen_number)

random.shuffle(password)
# random.shuffle fonksiyonuyla listenin elemanlarını karıştırabilirsin.
print("".join(password))
# " ".join(LİST) fonksiyonuyla küme elemanlarının arasını boşlukla açabilir, kelime veya harf yerleştirebilir veya bitişik yazılmalarını sağlayabilirsin.

  
  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P