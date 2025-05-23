listn = ["abc", "def", ["ghi", "jkl"]]
fl = []
for item in listn:
    if isinstance(item, list):
        fl.extend(item)
    else:
        fl.append(item)
final = list("".join(fl))
print(final)
