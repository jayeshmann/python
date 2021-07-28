"""
Transpose of a matrix
"""


def transpose(matrix):
    for i in range(len(matrix[0])):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# 1 2 3
# 4 5 6
# 7 8 9

#  1 4 7
#  2 5 8
#  3 6 9
