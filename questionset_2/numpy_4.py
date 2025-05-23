import numpy as np
arr = np.random.randint(1, 100, (5, 5))
border = []
border.extend(arr[0, :])
for i in range(1, 4):
    border.append(arr[i, 0])     
    border.append(arr[i, -1])    
border.extend(arr[-1, :])
print(border)
