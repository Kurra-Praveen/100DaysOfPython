year = int(input("enter the year"))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("its a leap year")
    elif year % 100 !=0:
        print("its a leap year")
    else:
        print("its not a leap year")
