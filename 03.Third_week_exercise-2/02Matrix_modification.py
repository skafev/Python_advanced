def make_matrix(num):
    matrix_maker = []
    for _ in range(num):
        i = [int(x) for x in input().split(' ')]
        matrix_maker.append(i)
    return matrix_maker
    # for r in range(rows):
    #     cols = list(map(int, input().split(" ")))
    #     matrix.append(cols)


def is_valid(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


def add_to_matrix(r, c, v):
    matrix[r][c] += v


def subtract_of_matrix(r, c, v):
    matrix[r][c] -= v


n = int(input())
matrix = make_matrix(n)

while True:
    command, *args = input().split(' ')
    if command == "END":
        for i in matrix:
            print(' '.join(map(str, i)))
        break
    row, col, value = args
    if is_valid(int(row), int(col)):
        if command == "Add":
            add_to_matrix(int(row), int(col), int(value))
        elif command == "Subtract":
            subtract_of_matrix(int(row), int(col), int(value))
    else:
        print("Invalid coordinates")
