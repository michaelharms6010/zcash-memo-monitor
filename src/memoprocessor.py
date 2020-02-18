import sys, json

f = open("memooutput.txt", "w")
txns = json.load(sys.stdin)

for t in txns:
    print(t["datetime"])
    print(t["amount"])
    print(t["memo"])


# f.write(sys.stdin)

print("Done!")