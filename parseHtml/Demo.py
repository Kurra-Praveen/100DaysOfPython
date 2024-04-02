import os

from bs4 import BeautifulSoup

files = os.path.join(os.getcwd(), "html")
data_files = list(os.walk(files))
file_path = data_files[0][0]
file_names = data_files[0][2]

data = {}
for each_file in file_names:
    with open(file_path + "\\" + each_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    element = soup.find(class_='test-list-item')

    test_cases = element.find_all("li")
    for each in test_cases:
        test_case_name = each.find_next(class_='name').getText()
        test_status = each.find_next(class_='badge pass-bg log float-right').getText()
        if test_case_name in data.keys():
            value = data[test_case_name]
            value.append(test_status)
            data[test_case_name] = value
        else:
            data[test_case_name] = [test_status]

print(data)
