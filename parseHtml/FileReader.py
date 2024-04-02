import os
from datetime import datetime

from bs4 import BeautifulSoup


class fileReader:

    def __init__(self):
        self.files = os.path.join(os.getcwd(), "html")
        self.data_files = list(os.walk(self.files))
        self.file_path = self.data_files[0][0]
        self.file_names = self.data_files[0][2]

    def getHtmlData(self):
        data = {}
        for each_file in self.file_names:
            with open(self.file_path + "\\" + each_file) as fp:
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

        return data

    def get_records(self, str_from_date, str_to_date):
        entireData = self.getHtmlData()
        for k, v in sorted(entireData.items()):
            if k > str_to_date:
                break
            if k >= str_from_date:
                yield k, v
