
year = int(input("Which year do you want to check? "))

c1 = year % 4
c2 = year % 100
c3 = year % 400

if c1 == 0:
    if c2 == 0:
        if c3 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

