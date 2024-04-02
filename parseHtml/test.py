from FileReader import fileReader
from flask import Flask, render_template

app = Flask("__name__")
reader = fileReader()
data = reader.getHtmlData()
allData = dict(reader.get_records('2023-01-10', '2023-01-11'))
dataSet = {}
for item in allData.items():
    dictData = item[1]
    for k, v in dictData.items():
        if k not in dataSet:
            dataSet[k] = v
        else:
            test_caseData = dataSet[k]
            test_caseData += v
            dataSet[k] = test_caseData

tabular_data = []
i = 1
for k, v in dataSet.items():
    temp = [i, k]
    pass_count = v.count('Pass')
    fail_count = len(v) - pass_count
    temp.append(pass_count)
    temp.append(fail_count)
    tabular_data.append(temp)
    i += 1
print(tabular_data)