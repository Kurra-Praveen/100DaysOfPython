from bs4 import BeautifulSoup
from datetime import datetime
with open("html/sample.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# element = soup.find(class_='test-list-item')
#
# test_cases = element.find_all("li")
#
# data = {}
# for each in test_cases:
#     test_case_name = each.find_next(class_='name').getText()
#     test_status = each.find_next(class_='badge pass-bg log float-right').getText()
#     data[test_case_name] = [test_status]
#
# print(data)

element = soup.find(class_='nav-right')

right_bar = element.find_all("li")
day = ['am', 'pm']
for each_element in right_bar:
    date = each_element.find_next("span").getText()
    day_rep = date[len(date) - 2:]
    if day_rep in day:
        #date.join("")
        s=date.replace(" ","").replace(",","")
        datetime_obj = datetime.strptime(s[:s.index(":") - 2],
                                         "%b%d%Y")
        date=str(datetime_obj).split(' ')[0]
        print(date)
