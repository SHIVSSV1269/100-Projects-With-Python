print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is you age?"))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 10
        print("Please pay $10")
    else:
        bill = 15
        print("Please pay $15.")
    want_photo = input("Do you want a photo ? Type Yes or No.")
    if want_photo == "Yes":
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
