import json

website = input("enter the websiteName")
emai = input("enter email")
passWord = input("enter password")


def createJson(websiteName, email, password):
    dta = {
        websiteName: {
            "email": email,
            "password": password
        }
    }
    try:
        with open("xyz.json", "r") as file:
            all_data = json.load(file)

    except FileNotFoundError:
        with open("xyz.json", "w") as file:
            json.dump(dta, file, indent=4)

    else:
        all_data.update(dta)

        with open("xyz.json", 'w') as file:
            json.dump(all_data, file, indent=4)


createJson(website, emai, passWord)

with open("xyz.json", "r") as data_file:
    data = json.load(data_file)

search_website = input("enter the website :")
try:
    user_database = data[search_website]
except KeyError:
    print("No data found")
else:
    print(user_database['email'])
    print(user_database['password'])
