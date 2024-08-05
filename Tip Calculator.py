#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
person = input("How many people to split the bill? ")

total_bill = float(bill) * (int(percentage) + 100) / 100 / int(person)
x = round(total_bill, 2)
x = "{:.2f}".format(x)
#Burdaki "{:.2f}".format olayı, bilgisayarın sonucu tam sayı hesapladığı takdirde sonucun 28.0 değil de 28.00 gibi gözükmesini sağlamak için. Format fonksiyonu deniliyor.
print("Each person should pay: $" + str(x))
