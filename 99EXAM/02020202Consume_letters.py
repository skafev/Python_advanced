UP_COMMAND = "up"
DOWN_COMMAND = "down"
LEFT_COMMAND = "left"
RIGHT_COMMAND = "right"
EMPTY_POSITION = "-"
PLAYER = "P"
def make_matrix():
    matrix_size = int(input())
    matrix = []
    for _ in range(matrix_size):
        row = list(input())
        matrix.append(row)
    return matrix


def find_the_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == PLAYER:
                return int(row), int(col)


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


text = input()
matrix = make_matrix()
player = find_the_player(matrix)
player_row = player[0]
player_col = player[1]
n = int(input())
count = 0
while count != n:
    command = input()
    if command == UP_COMMAND:
        potential_row = player_row - 1
        if is_valid(potential_row, player_col):
            if matrix[potential_row][player_col] == EMPTY_POSITION:
                matrix[potential_row][player_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = potential_row
                player_col = player_col
            else:
                text += matrix[potential_row][player_col]
                matrix[potential_row][player_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = potential_row
                player_col = player_col
        else:
            text = text[:-1]

    elif command == DOWN_COMMAND:
        potential_row = player_row + 1
        if is_valid(potential_row, player_col):
            if matrix[potential_row][player_col] == EMPTY_POSITION:
                matrix[potential_row][player_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = potential_row
                player_col = player_col
            else:
                text += matrix[potential_row][player_col]
                matrix[potential_row][player_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = potential_row
                player_col = player_col
        else:
            text = text[:-1]

    elif command == LEFT_COMMAND:
        potential_col = player_col - 1
        if is_valid(player_row, potential_col):
            if matrix[player_row][potential_col] == EMPTY_POSITION:
                matrix[player_row][potential_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = player_row
                player_col = potential_col
            else:
                text += matrix[player_row][potential_col]
                matrix[player_row][potential_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = player_row
                player_col = potential_col
        else:
            text = text[:-1]

    elif command == RIGHT_COMMAND:
        potential_col = player_col + 1
        if is_valid(player_row, potential_col):
            if matrix[player_row][potential_col] == EMPTY_POSITION:
                matrix[player_row][potential_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = player_row
                player_col = potential_col
            else:
                text += matrix[player_row][potential_col]
                matrix[player_row][potential_col] = PLAYER
                matrix[player_row][player_col] = EMPTY_POSITION
                player_row = player_row
                player_col = potential_col
        else:
            text = text[:-1]

    count += 1

print(text)
for x in matrix:
    print("".join(x))
