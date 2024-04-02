from flask import Flask, render_template, request, make_response
from FileReader import fileReader

app = Flask(__name__)
reader = fileReader()
data = []
heading = ["sl no", "test case name", "pass count", "fail count"]


def getRecords(fromDate, toDate):
    allData = dict(reader.get_records(fromDate, toDate))
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
        temp.append(len(v))

        tabular_data.append(temp)

        i += 1
    return tabular_data


@app.route('/', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        from_date = request.form['from_date']
        to_date = request.form['to_date']
        global data
        data = getRecords(from_date, to_date)
        return render_template("table.html", headings=heading,
                               data=data)
    return render_template('table.html')


@app.route('/download_file')
def download_file():
    html = render_template('table.html', headings=heading, data=data)
    response = make_response(html)
    response.headers["Content-Disposition"] = "attachment; filename=table.html"
    return response


if __name__ == "__main__":
    app.run(debug=True)
