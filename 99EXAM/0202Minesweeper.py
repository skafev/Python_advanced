import re
BOMB = "*"


def make_matrix():
    matrix_size = int(input())
    matrix = []
    for r in range(matrix_size):
        matrix.append([])
        for c in range(matrix_size):
            matrix[r].append(0)
    return matrix


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


matrix = make_matrix()
number_of_bombs = int(input())
counter = 0
while counter < number_of_bombs:
    bombs = list(map(lambda x: int(x), input()[1:][:-1].split(", ")))
    bombs_row = bombs[0]
    bombs_column = bombs[1]
    matrix[bombs_row][bombs_column] = BOMB
    rows = [0, -1, -1, -1, 0, +1, +1, +1]
    cols = [+1, +1, 0, -1, -1, -1, 0, +1]
    for index in range(len(rows)):
        potential_row = rows[index] + bombs_row
        potential_column = cols[index] + bombs_column
        if is_valid(potential_row, potential_column):
            if matrix[potential_row][potential_column] == BOMB:
                continue
            matrix[potential_row][potential_column] += 1

    counter += 1

for x in matrix:
    print(' '.join(map(str, x)))
