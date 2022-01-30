BUNNY = "B"
TRAP = "X"


def make_matrix(matrix_size):
    matrix = []
    for row_index in range(matrix_size):
        row = list(input().split())
        matrix.append(row)
    return matrix


def search_for_the_bunny(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def is_valid(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


def up_move(r, c):
    up_count = 0
    i = 1
    while True:
        try:
            if matrix[r - i][c] != TRAP and is_valid(r - i, c):
                up_count += int(matrix[int(r - i)][int(c)])
                i += 1
            else:
                break
        except IndexError:
            return up_count
    return up_count


def down_move(r, c):
    down_count = 0
    i = 1
    while True:
        try:
            if matrix[r + i][c] != TRAP and is_valid(r + i, c):
                down_count += int(matrix[int(r + i)][int(c)])
                i += 1
            else:
                break
        except IndexError:
            return down_count
    return down_count


def right_move(r, c):
    right_count = 0
    i = 1
    while True:
        try:
            if matrix[r][c + i] != TRAP and is_valid(r, c + i):
                right_count += int(matrix[int(r)][int(c + i)])
                i += 1
            else:
                break
        except IndexError:
            return right_count
    return right_count


def left_move(r, c):
    left_count = 0
    i = 1
    while True:
        try:
            if matrix[r][c - i] != TRAP and is_valid(r, c - i):
                left_count += int(matrix[int(r)][int(c - i)])
                i += 1
            else:
                break
        except IndexError:
            return left_count
    return left_count


matrix_size = int(input())
matrix = make_matrix(matrix_size)
row, col = search_for_the_bunny(matrix, BUNNY)
up = up_move(row, col)
down = down_move(row, col)
right = right_move(row, col)
left = left_move(row, col)
result = max(up, down, left, right)
if result == up:
    print('up')
    i = 1
    for _ in range(row, 0, -1):
        print([row - i, col])
        i += 1
elif result == down:
    print('down')
    i = 1
    for _ in range(row, matrix_size - 1):
        print([row + i, col])
        i += 1
elif result == left:
    print("left")
    i = 1
    for _ in range(col, 0, -1):
        print([row, col - i])
        i += 1
else:
    print("right")
    i = 1
    for _ in range(col, matrix_size - 1):
        print([row, col + i])
        i += 1

print(result)
