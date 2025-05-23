n = input("Enter a natural number Greater Than 0 ")
if n.isdigit() and  int(n) >= 1:
    n = int(n)
    for i in range(1, n + 1):
        sum = 0
        for j in range(1, i + 1):
            sum += j**2
        print(sum)
else:
    print("Invalid input")
