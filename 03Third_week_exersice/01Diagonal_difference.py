def make_matrix():
    matrix_size = int(input())
    matrix = []
    for row_index in range(matrix_size):
        row = list(map(int, input().split(" ")))
        matrix.append(row)
    return matrix


def get_primary_diagonal(matrix):
    primary_diagonal = 0
    for i in range(len(matrix)):
        primary_diagonal += matrix[i][i]
    return primary_diagonal


def get_secondary_diagonal(matrix):
    secondary_diagonal = 0
    size = len(matrix)
    for i in range(size):
        secondary_diagonal += matrix[i][size - i - 1]
    return secondary_diagonal


def print_result(primary, secondary):
    total = abs(primary - secondary)
    print(total)


matrix = make_matrix()
print_result(get_primary_diagonal(matrix), get_secondary_diagonal(matrix))
