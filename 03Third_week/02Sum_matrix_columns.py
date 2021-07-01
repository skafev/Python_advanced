def make_matrix():
    rows_count, columns_count = map(int, input().split(", "))
    matrix = []
    for row_index in range(rows_count):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix


def get_column_sum(matrix):
    result = []
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    for c in range(columns_count):
        sum_columns = 0
        for r in range(rows_count):
            sum_columns += matrix[r][c]
        result.append(sum_columns)
    return result


matrix = make_matrix()
[print(x) for x in get_column_sum(matrix)]
