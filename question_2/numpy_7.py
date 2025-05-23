def determinant(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]

    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det

matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

print( determinant(matrix))