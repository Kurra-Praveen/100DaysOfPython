height = int(input("Enter your height"))
bill = 0
if height >= 120:
    print("you can ride ")
    age = int(input("enter your age "))
    if age >=45 and age <=55:
        bill=0
    elif age < 12:
        print("you have to pay $5 ticket")
        bill += 5
    elif 12 <= age <= 18:
        print("you pay $7 ticket")
        bill += 7
    else:
        print("you have to pay 17")
        bill += 17
    photos = input("do want to take photos y / n")
    if photos == y:
        bill += 3

    print(bill)
else:
    print("sorry, you are not eligible ")