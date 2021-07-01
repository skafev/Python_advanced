def make_matrix():
    matrix_size = int(input())
    matrix = []
    for row_index in range(matrix_size):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix


def get_primary_diagonal_sum(matrix):
    primary_diagonal_sum = 0
    for i in range(len(matrix)):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum


# secondary_diagonal
# def get_secondary_diagonal_sum(matrix):
#     secondary_diagonal = 0
#     for r in range(len(matrix)):
#         for c in range(len(matrix)):
#             if r >= c:
#                 secondary_diagonal += matrix[r][c]
#     return secondary_diagonal
#


matrix = make_matrix()
print(get_primary_diagonal_sum(matrix))
