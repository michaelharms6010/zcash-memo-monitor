import sys, json
import requests

# URL = "https://be.zeitpages.com/board"
URL = "https://zeitpages-staging.herokuapp.com/board"

f = open("memooutput.txt", "w")
txns = json.load(sys.stdin)
txnlist = []
headers = {"content-type": "application/json"}

for t in txns:
    datetime = t["datetime"]
    amount = t["amount"]
    memo = t["memo"]
    params = {"datetime": datetime, "amount": amount, "memo": memo}
    txnlist.append(params)

# if txn is new:
for post in txnlist:
    r = requests.post(url = URL, data=json.dumps(post), headers=headers)
    print(r)



# f.write(sys.stdin)

print("Done!")