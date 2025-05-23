inStr = input("enter a string")
length = len(inStr)
count = {}
for i in range(0,length-1):
    count[inStr[i]] = inStr.count(inStr[i])

for k, v in count.items():
    print(f"{k}: {v}")