def make_matrix():
    matrix_size = int(input())
    matrix = []
    for row_index in range(matrix_size):
        row = input()
        matrix.append(row)
    return matrix


def find_symbol(matrix, symbol):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if symbol == matrix[r][c]:
                return r, c


def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = make_matrix()
symbol = input()
print_result(find_symbol(matrix, symbol), symbol)
