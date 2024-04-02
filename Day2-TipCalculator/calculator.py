print("Welcome to the tip calculator")
bill = float(input("What was the total Bill? $ "))
numberOfPersons = int(input("how members to split the bill"))
tip = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))
totalBill = (tip / 100 * bill) + bill
eachPersonBill = round(totalBill / numberOfPersons, 2)
eachPersonBill: str= "{:.2f}".format(totalBill)
print(f"Each person should pay :${eachPersonBill}")
