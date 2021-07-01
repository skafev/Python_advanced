def make_matrix():
    rows_count, columns_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix


def get_current_biggest_submatrix(matrix, row_index, column_index, size):
    current_biggest = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            current_biggest += matrix[r][c]
    return current_biggest


matrix = make_matrix()
size = 2
biggest_square = 0
best_row_index = 0
best_column_index = 0

for row in range(len(matrix) - size + 1):
    for column in range(len(matrix[row]) - size + 1):
        current_sum = get_current_biggest_submatrix(matrix, row, column, size)
        if biggest_square < current_sum:
            biggest_square = current_sum
            best_row_index = row
            best_column_index = column

for r in range(best_row_index, best_row_index + size):
    row = []
    for c in range(best_column_index, best_column_index + size):
        row.append(matrix[r][c])
    print(" ".join(str(x) for x in row))

print(biggest_square)