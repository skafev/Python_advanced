import sys
rows_count, columns_count = map(int, input().split(" "))


def make_matrix():
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    return matrix


matrix = make_matrix()
final_sum = -sys.maxsize
final_matrix = []
for r in range(rows_count - 2):
    for c in range(columns_count - 2):
        try:
            first_row = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]]
            second_row = [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]]
            third_row = [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
            current_sum = sum(first_row) + sum(second_row) + sum(third_row)
            if current_sum > final_sum:
                final_sum = current_sum
                final_matrix.clear()
                final_matrix.append(first_row)
                final_matrix.append(second_row)
                final_matrix.append(third_row)
        except IndexError:
            pass
print(f"Sum = {final_sum}")
for i in final_matrix:
    print(" ".join(map(str, i)))
