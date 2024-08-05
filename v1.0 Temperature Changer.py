print("Welcome to the Temperature Generator!")

# gireceği sıcaklık tipi sorulacak
# değer girilecek
# istediği değer sorulacak
# sonuç ekrana gelecek
# devam etmek isteyip istemediği sorulacak

def tempChanger(temp, tempType, targetType):
    if tempType == "kelvin":
        if targetType == "celcius":
            return temp - 273
        if targetType == "fahrenheit":
            return (temp - 273) * 1.8 + 32
    if tempType == "celcius":
        if targetType == "kelvin":
            return temp + 273
        if targetType == "fahrenheit":
            return temp * 1.8 + 32
    if tempType == "fahrenheit":
        if targetType == "kelvin":
            return (temp - 32) / 1.8 + 273
        if targetType == "celcius":
            return (temp - 32) / 1.8


commandOver = False
while not commandOver:
    tempType = input("What's the type of temperature you entered in? Is it Kelvin, Celcius or Fahrenheit?\n")
    temp = int(input("What is the temperature?\n"))
    targetType = input("Whats your choice for temperature type? Kelvin, Celcius or Fahrenheit?\n")
    result = round(tempChanger(temp, tempType, targetType), 2)
    target_result = targetType.title()
    print(f"The result is {result} {target_result}.")
    willContinue = input("Do you want to continue to Temperature Changer? Yes or no.\n")
    if willContinue == "no":
        commandOver = True
        print("Goodbye. Have a great day!")


