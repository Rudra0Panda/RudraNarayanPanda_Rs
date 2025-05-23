arr = [1, [2, [3, [4, []]]], 5]
count = 0
current = arr
while isinstance(current, list):
    found = False
    for item in current:
        if isinstance(item, list):
            current = item
            count += 1
            found = True
            break
    if not found:
        break

print("Depth:", count + 1)  
