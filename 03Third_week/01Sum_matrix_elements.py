def make_matrix():
    rows_count, columns_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix


def matrix_sum(matrix):
    matrix_sum = 0
    for r in range(len(matrix)):
        row = matrix[r]
        for c in range(len(row)):
            matrix_sum += row[c]
    return matrix_sum


matrix = make_matrix()
print(matrix_sum(matrix))
print(matrix)
