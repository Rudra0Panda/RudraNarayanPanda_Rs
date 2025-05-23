n = input("enter a num")
n_bin = bin(int(n))[2::]
if n_bin.count("1") == 1 :
    print("num is power of 2")
else:
    print("not a power of 2")

if n > 0 and (n & (n - 1)) == 0:
    print("num is a power of 2")
else:
    print(" not a power of 2")
