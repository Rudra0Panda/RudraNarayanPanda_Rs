import numpy as np
arr = np.array([1, 2, 3])
nums = np.array([4, 5, 6])
evens = nums[nums % 2 == 0]
arr = np.append(arr, evens)
print(arr)
