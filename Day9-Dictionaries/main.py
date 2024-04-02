bidders = {}


def highestBid(bidders):
    maximum = 0
    name = ""
    for bid in bidders:
        if bidders[bid] > maximum:
            maximum = bidders[bid]
            name = bid
    print(f"{maximum}  is the highest bid by {name}")


while True:
    name = input("enter your name :")
    price = int(input("enter your bid price "))
    bidders[name] = price
    newEntry = input("is there anyone to bid , type y/n ").lower()
    if newEntry == "y":
        continue
    else:
        highestBid(bidders)
        break

print(bidders)







# travelLog = [
#     {
#         "country": "India",
#         "citiesVisited": ["Vizag", "Banglore", "Hyderabad"],
#         "noOfVisits": 20
#     },
#     {
#         "country": "Russia",
#         "citiesVisited": ["Moscow", "Bankcok", "chile"],
#         "noOfVisits": 2
#     }
#
# ]
#
# print(travelLog)
# def modifyDetails(country, noOfVisits, citiesVisted):
#     newDict = {}
#     newDict["country"] = country
#     newDict["noOfVisits"] = noOfVisits
#     newDict["citiesVisited"] = citiesVisted
#     travelLog.append(newDict)
#
#
# modifyDetails("japan", 3, ["Tokyo", "sighchan"])
# print(travelLog)


# scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }
#
# for score in scores:
#     if scores[score] > 90:
#         scores[score] = "Outstanding"
#     elif 80 < scores[score] <= 90:
#         scores[score] = "Exceeds Expectations"
#     elif 70 < scores[score] <= 80:
#         scores[score] = "Acceptable"
#     else:
#         scores[score] = "Fail"
#
# print(scores)
