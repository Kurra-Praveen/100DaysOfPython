import random
import json

import pandas

# data=pandas.read_csv("french_words.csv")
# alldata=data.to_dict(orient="records")
# with open("xyz.json","w") as file:
#     json.dump(alldata,file,indent=4)

with open("xyz.json") as file2:
    jsondata = json.load(file2)
entries = {
}
randomentry = random.choice(jsondata)
randomentry2=random.choice(jsondata)
print(randomentry)
# entries += randomentry
entries["0"]=randomentry2
entries["1"]=randomentry
print(entries)
