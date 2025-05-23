n = input("enter a num")
sum = 0 
while n.isdigit():
    sum += int(n)  
    n = input("enter a num to continue")
print(sum)    