import numpy as np
matrix = np.zeros((5, 5), dtype=int)
for i in range(5):
    matrix[i][i] = i + 1  

print(matrix)