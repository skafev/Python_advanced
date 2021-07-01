KING = "K"
QUEEN = "Q"


def make_matrix():
    rows = 0
    matrix = []
    while rows != 8:
        matrix_size = input().split()
        matrix.append(matrix_size)
        rows += 1
    return matrix


def is_valid(row, col):
    if 0 <= row < len(ches_board) and 0 <= col < len(ches_board):
        return True
    return False


def find_the_king(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == KING:
                return row, col


queens = []
ches_board = make_matrix()
king_found = find_the_king(ches_board)
king_row = king_found[0]
king_col = king_found[1]
# right
for index in range(king_col, len(ches_board)):
    if ches_board[king_row][index] == QUEEN:
        queens.append([king_row, index])
        break
# left
for index in range(king_col, -1, -1):
    if ches_board[king_row][index] == QUEEN:
        queens.append([king_row, index])
        break
# up
for index in range(king_row, -1, -1):
    if ches_board[index][king_col] == QUEEN:
        queens.append([index, king_col])
        break
# down
for index in range(king_row, len(ches_board)):
    if ches_board[index][king_col] == QUEEN:
        queens.append([index, king_col])
        break

count = 1
for index in range(king_row, -1, -1):
    r = king_row - count
    c = king_col + count
    if is_valid(r, c):
        if ches_board[r][c] == QUEEN:
            queens.append([r, c])
            count = 1
            break
    else:
        count = 1
        break
    count += 1

for index in range(king_row, -1, -1):
    r = king_row - count
    c = king_col - count
    if is_valid(r, c):
        if ches_board[r][c] == QUEEN:
            queens.append([r, c])
            count = 1
            break
    else:
        count = 1
        break
    count += 1

for index in range(king_row, -1, -1):
    r = king_row + count
    c = king_col - count
    if is_valid(r, c):
        if ches_board[r][c] == QUEEN:
            queens.append([r, c])
            count = 1
            break
    else:
        count = 1
        break
    count += 1

for index in range(king_row, len(ches_board)):
    r = king_row + count
    c = king_col + count
    if is_valid(r, c):
        if ches_board[r][c] == QUEEN:
            queens.append([r, c])
            count = 1
            break
    else:
        count = 1
        break
    count += 1
if not queens:
    print(f"The king is safe!")
else:
    print(*queens, sep="\n")
