import sys, json
import requests
import ast

# URL = "https://be.zeitpages.com/board"
URL = "https://zeitpages-staging.herokuapp.com/board"

oldtxns = open("memooutput.txt", "r")
records = []
for i in oldtxns:
    records.append(ast.literal_eval(i))

f = open("memooutput.txt", "a")
txns = json.load(sys.stdin)
txnlist = []
headers = {"content-type": "application/json"}
for t in txns:
    datetime = t["datetime"]
    amount = t["amount"]
    memo = t["memo"]
    params = {"datetime": datetime, "amount": amount, "memo": memo}
    txnlist.append(params)

times = [int(i["datetime"]) for i in records]

for post in txnlist:
    if post["memo"] == None or post["amount"] < 100000:
        continue
    elif post["datetime"] in times:
        continue
    else:
        r = requests.post(url = URL, data=json.dumps(post), headers=headers)
        print(r)
        f.write(str(post)+ "\n")

print("Done!")