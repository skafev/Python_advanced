rows_count, columns_count = map(int, input().split(" "))


def make_matrix():
    matrix = []
    for row_index in range(rows_count):
        row = input().split(" ")
        matrix.append(row)
    return matrix


matrix = make_matrix()
count = 0
for r in range(rows_count- 1):
    for c in range(columns_count - 1):
        current_char = matrix[r][c]
        right_char = matrix[r][c + 1]
        down_char = matrix[r + 1][c]
        down_right_char = matrix[r + 1][c + 1]
        current_square = current_char, right_char, down_char, down_right_char
        equal_char = set(current_square)
        if len(equal_char) == 1:
            count += 1

print(count)
