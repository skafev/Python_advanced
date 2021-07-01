KNIGHT = "K"


def make_matrix():
    matrix_size = int(input())
    matrix = []
    for row_index in range(matrix_size):
        row = list(input())
        matrix.append(row)
    return matrix


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def calculate_kills(matrix, row, column):
    kills = 0
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = column + cols[index]
        if is_valid(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == KNIGHT:
                kills += 1

    return kills


matrix = make_matrix()
removed_counter = 0
while True:
    max_kills = 0
    knight_position = ""

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == KNIGHT:
                kills = calculate_kills(matrix, r, c)
                if kills > max_kills:
                    max_kills = kills
                    knight_position = [r, c]
    if knight_position:
        matrix[knight_position[0]][knight_position[1]] = "0"
        removed_counter += 1
    else:
        break

print(removed_counter)
