import os
from datetime import datetime

from bs4 import BeautifulSoup
from collections import OrderedDict

files = os.path.join(os.getcwd(), "html")
data_files = list(os.walk(files))
file_path = data_files[0][0]
file_names = data_files[0][2]

data = {}
for each_file in file_names:
    with open(file_path + "\\" + each_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    element = soup.find(class_='nav-right')
    right_bar = element.find_all("li")
    day = ['am', 'pm']
    date = ""
    for each_element in right_bar:
        date = each_element.find_next("span").getText()
        day_rep = date[len(date) - 2:]
        if day_rep in day:
            # sample_date = date.split(',')[0]
            # date = sample_date
            s = date.replace(" ", "").replace(",", "")
            datetime_obj = datetime.strptime(s[:s.index(":") - 2],
                                             "%b%d%Y")
            date = str(datetime_obj).split(' ')[0]

    element = soup.find(class_='test-list-item')
    test_cases = element.find_all("li")

    for each in test_cases:
        test_case_name = each.find_next(class_='name').getText()
        test_status = each.find_next(class_='badge pass-bg log float-right').getText()
        if date in data.keys():
            test_data = data[date]
            if test_case_name in test_data.keys():
                value = test_data[test_case_name]
                value.append(test_status)
                test_data[test_case_name] = value
            else:
                test_data[test_case_name] = [test_status]

            data[date] = test_data

        else:
            test_in = {test_case_name: [test_status]}
            data[date] = test_in


def get_records(dict_history, str_from_date, str_to_date):
    for k, v in sorted(dict_history.items()):
        if k > str_to_date:
            break
        if k >= str_from_date:
            yield k, v


print(data)
# print (data.items())
# print(list(get_records(data, '2023-01-10', '2023-01-11')))
