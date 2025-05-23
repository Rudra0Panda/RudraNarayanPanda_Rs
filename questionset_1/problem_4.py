n = {}
keys = int(input("enter number of keys "))
for x in range(keys):
    key = input("enter key ")
    values =  input("enter values separated by space ")
    valuesList = list(map(int, values.split()))
    n[key] = valuesList

rept = []
for key in n:
    templist = []
    for value in n[key]:
        if value not in rept:
            templist.append(value)
            rept.append(value)
    n[key] = templist

for k, v in n.items():
    print(f"{k}:{v}")