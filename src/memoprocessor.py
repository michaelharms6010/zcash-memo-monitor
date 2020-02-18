import sys, json
import requests

URL = "https://be.zeitpages.com/board"

f = open("memooutput.txt", "w")
txns = json.load(sys.stdin)
txnlist = []

for t in txns:
    datetime = t["datetime"]
    amount = t["amount"]
    memo = t["memo"]
    params = {"datetime": datetime, "amount": amount, "memo": memo}
    txnlist.append(params)

print(txnlist)
# f.write(sys.stdin)

print("Done!")