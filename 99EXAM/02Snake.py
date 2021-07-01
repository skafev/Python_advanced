SNAKE = "S"
EMPTY_POSITION = "-"
FOOD = "*"
TRAIL = "."
BURROWS = "B"
UP_COMMAND = 'up'
DOWN_COMMAND = 'down'
LEFT_COMMAND = 'left'
RIGHT_COMMAND = 'right'


def make_matrix():
    matrix_size = int(input())
    matrix = []
    for _ in range(matrix_size):
        row = list(input())
        matrix.append(row)
    return matrix


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


food_quantity = 0
matrix = make_matrix()
in_territory = True
snake_row = 0
snake_column = 0

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == SNAKE:
            snake_row = int(r)
            snake_column = int(c)
            break

while in_territory:
    command = input()

    if command == UP_COMMAND:
        current_row = snake_row - 1
        current_column = snake_column
        if is_valid(current_row, current_column):
            if matrix[current_row][current_column] == FOOD:
                food_quantity += 1
                matrix[current_row][current_column] = SNAKE
                matrix[current_row + 1][current_column] = TRAIL
                snake_row -= 1
            elif matrix[current_row][current_column] == BURROWS:
                end_of_burrows_row = 0
                end_of_burrows_column = 0
                for b in range(len(matrix)):
                    for j in range(len(matrix)):
                        if matrix[b][j] == BURROWS:
                            if b != current_row and j != current_column:
                                end_of_burrows_row = b
                                end_of_burrows_column = j
                matrix[current_row][current_column] = TRAIL
                matrix[end_of_burrows_row][end_of_burrows_column] = SNAKE
                matrix[current_row + 1][current_column] = TRAIL
                snake_row = end_of_burrows_row
                snake_column = end_of_burrows_column
            else:
                matrix[current_row][current_column] = SNAKE
                matrix[current_row + 1][current_column] = TRAIL
                snake_row -= 1
        else:
            matrix[current_row + 1][current_column] = TRAIL
            in_territory = False

    elif command == DOWN_COMMAND:
        current_row = snake_row + 1
        current_column = snake_column
        if is_valid(current_row, current_column):
            if matrix[current_row][current_column] == FOOD:
                food_quantity += 1
                matrix[current_row][current_column] = SNAKE
                matrix[current_row - 1][current_column] = TRAIL
                snake_row += 1
            elif matrix[current_row][current_column] == BURROWS:
                end_of_burrows_row = 0
                end_of_burrows_column = 0
                for b in range(len(matrix)):
                    for j in range(len(matrix)):
                        if matrix[b][j] == BURROWS:
                            if b != current_row and j != current_column:
                                end_of_burrows_row = b
                                end_of_burrows_column = j
                matrix[current_row][current_column] = TRAIL
                matrix[end_of_burrows_row][end_of_burrows_column] = SNAKE
                matrix[current_row - 1][current_column] = TRAIL
                snake_row = end_of_burrows_row
                snake_column = end_of_burrows_column
            else:
                matrix[current_row][current_column] = SNAKE
                matrix[current_row - 1][current_column] = TRAIL
                snake_row += 1
        else:
            matrix[current_row - 1][current_column] = TRAIL
            in_territory = False

    elif command == LEFT_COMMAND:
        current_row = snake_row
        current_column = snake_column - 1
        if is_valid(current_row, current_column):
            if matrix[current_row][current_column] == FOOD:
                food_quantity += 1
                matrix[current_row][current_column] = SNAKE
                matrix[current_row][current_column + 1] = TRAIL
                snake_column -= 1
            elif matrix[current_row][current_column] == BURROWS:
                end_of_burrows_row = 0
                end_of_burrows_column = 0
                for b in range(len(matrix)):
                    for j in range(len(matrix)):
                        if matrix[b][j] == BURROWS:
                            if b != current_row and j != current_column:
                                end_of_burrows_row = b
                                end_of_burrows_column = j
                matrix[current_row][current_column] = TRAIL
                matrix[end_of_burrows_row][end_of_burrows_column] = SNAKE
                matrix[current_row][current_column + 1] = TRAIL
                snake_row = end_of_burrows_row
                snake_column = end_of_burrows_column
            else:
                matrix[current_row][current_column] = SNAKE
                matrix[current_row][current_column + 1] = TRAIL
                snake_column -= 1
        else:
            matrix[current_row][current_column + 1] = TRAIL
            in_territory = False

    elif command == RIGHT_COMMAND:
        current_row = snake_row
        current_column = snake_column + 1
        if is_valid(current_row, current_column):
            if matrix[current_row][current_column] == FOOD:
                food_quantity += 1
                matrix[current_row][current_column] = SNAKE
                matrix[current_row][current_column - 1] = TRAIL
                snake_column += 1
            elif matrix[current_row][current_column] == BURROWS:
                end_of_burrows_row = 0
                end_of_burrows_column = 0
                for b in range(len(matrix)):
                    for j in range(len(matrix)):
                        if matrix[b][j] == BURROWS:
                            if b != current_row and j != current_column:
                                end_of_burrows_row = b
                                end_of_burrows_column = j
                matrix[current_row][current_column] = TRAIL
                matrix[end_of_burrows_row][end_of_burrows_column] = SNAKE
                matrix[current_row][current_column - 1] = TRAIL
                snake_row = end_of_burrows_row
                snake_column = end_of_burrows_column
            else:
                matrix[current_row][current_column] = SNAKE
                matrix[current_row][current_column - 1] = TRAIL
                snake_column += 1
        else:
            matrix[current_row][current_column - 1] = TRAIL
            in_territory = False
    if food_quantity == 10:
        break

if not in_territory:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
print(*["".join(x) for x in matrix], sep="\n")
