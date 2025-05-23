credit_number = "1234-5678-9012-3456"
# [start : end : step ]
print(credit_number[0]) #0
print(credit_number[0:4]) # 1234
print(credit_number[5:9]) # 5678
print(credit_number[5:]) # 5678-9012-3456
print(credit_number[-1]) # 6 
print(credit_number[::2]) # = [0 : -1 : 2 ] # every second char in the string # 13-6891-46 
print(credit_number[-4:-1:1]) # 345 
print(credit_number[-1:-5:-1] ) # use -1 steps in case of negative inedx # 6543