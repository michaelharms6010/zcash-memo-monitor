import sys, json
import requests
import ast
import codecs
import time



URL = "https://be.zecpages.com/board"
# URL = "https://zeitpages-staging.herokuapp.com/board"

with open("memooutput.txt", "r") as oldtxns:
    records = []
    for i in oldtxns:
        records.append(ast.literal_eval(i))

    with open("memooutput.txt", "a") as f:
        txns = json.load(sys.stdin)
        txnlist = []
        headers = {"content-type": "application/json", "Authorization": "admin token goes here"}
        for t in txns:
            txid = t["txid"]
            amount = int(t["amount"] * 100000000)
            memo = codecs.decode(t["memo"], "hex").decode("windows-1252").replace("\x00", "")
            datetime= int(time.time() * 1000)
            params = {"txid": txid, "amount": amount, "memo": memo, "datetime": datetime}
            txnlist.append(params)

        times = [i["txid"] for i in records]

        for post in txnlist:
            if post["memo"] == None or post["amount"] < 100000:
                continue
            elif post["txid"] in times:
                continue
            else:
                r = requests.post(url = URL, data=json.dumps(post), headers=headers)
                print(r)
                f.write(str(post)+ "\n")

    print("Done!")