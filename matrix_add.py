matrix1 = [ 
    [2, -2],
    [5, 3] 
    ]

matrix2 = [
    [5, 2],
    [1, 0]
]


#initialize resulting matrix
height = len(matrix1)
width = len(matrix1[0])
result = []
for i in range(height):
    result.append([])
    for j in range(width):
        result[i].append(None)

#fill in matrix
for i in range(height):
    for j in range(width):
        cell1 = matrix1[i][j]
        cell2 = matrix2[i][j]
        cell = cell1 + cell2

        result[i][j] = cell1 + cell2
print result
        