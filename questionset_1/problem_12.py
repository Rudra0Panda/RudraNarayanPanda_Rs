tr = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
arr = []
for t in tr:
    sum = 0.0 
    for x in t :
        sum += x
    arr.append(sum / len(t))
print(arr)