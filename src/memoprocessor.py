import sys, json
import requests

# URL = "https://be.zeitpages.com/board"
URL = "https://zeitpages-staging.herokuapp.com/board"

f = open("memooutput.txt", "w")
txns = json.load(sys.stdin)
txnlist = []
headers = {"content-type": "application/json"}
f.write("[")
first = True
for t in txns:
    datetime = t["datetime"]
    amount = t["amount"]
    memo = t["memo"]
    params = {"datetime": datetime, "amount": amount, "memo": memo}
    txnlist.append(params)
    if first:
        f.write(str(params))
    else:
        f.write("," + str(params))

f.write("]")
# if txn is new:

g = requests.get(url = URL)
postlist = g.json()
times = [int(i["datetime"]) for i in postlist]
print(times)

for post in txnlist:
    if post["memo"] == None or post["amount"] < 100000:
        continue
    elif post["datetime"] in times:
        continue
    else:
        r = requests.post(url = URL, data=json.dumps(post), headers=headers)
        print(r)



# f.write(sys.stdin)

print("Done!")