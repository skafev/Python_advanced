def make_matrix():
    matrix = []
    for _ in range(5):
        row = input().split()
        matrix.append(row)
    return matrix


def search_in_matrix(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def search_targets(matrix, search):
    count = 0
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                count += 1
    return count


def is_valid(r, c):
    if 0 <= r < len(matrix) and 0 <= c < len(matrix):
        return True
    return False


matrix = make_matrix()
row, col = search_in_matrix(matrix, "A")
all_targets = search_targets(matrix, "x")
target_positions = []
n = int(input())

for i in range(n):
    act, direction, *args = input().split()

    if act == "move":
        steps = [int(x) for x in args]
        if direction == 'right':
            if is_valid(row, col + steps[0]):
                if matrix[row][col + steps[0]] == ".":
                    matrix[row][col] = "."
                    col = col + steps[0]

        elif direction == 'left':
            if is_valid(row, col - steps[0]):
                if matrix[row][col - steps[0]] == ".":
                    matrix[row][col] = "."
                    col = col - steps[0]

        elif direction == 'up':
            if is_valid(row - steps[0], col):
                if matrix[row - steps[0]][col] == ".":
                    matrix[row][col] = "."
                    row = row - steps[0]

        elif direction == "down":
            if is_valid(row + steps[0], col):
                if matrix[row + steps[0]][col] == ".":
                    matrix[row][col] = "."
                    row = row + steps[0]

    elif act == "shoot":
        j = 1
        if direction == "right":
            for _ in range(col, 4):
                if is_valid(row, col + j):
                    if matrix[row][col + j] == "x":
                        target_positions.append([row, col + j])
                        matrix[row][col + j] = "."
                        break
                j += 1
        elif direction == "down":
            for _ in range(row, 4):
                if is_valid(row + j, col):
                    if matrix[row + j][col] == "x":
                        target_positions.append([row + j, col])
                        matrix[row + j][col] = "."
                        break
                j += 1
        elif direction == "up":
            for _ in range(row, 0, -1):
                if is_valid(row - j, col):
                    if matrix[row - j][col] == "x":
                        target_positions.append([row - j, col])
                        matrix[row - j][col] = "."
                        break
                j += 1
        elif direction == "left":
            for _ in range(col, 0, -1):
                if is_valid(row, col - j):
                    if matrix[row][col - j] == "x":
                        target_positions.append([row, col - j])
                        matrix[row][col - j] = "."
                        break
                j += 1
    if all_targets == len(target_positions):
        break

if all_targets == len(target_positions):
    print(f"Training completed! All {all_targets} targets hit.")
else:
    print(f"Training not completed! {all_targets - len(target_positions)} targets left.")

print(*target_positions, sep="\n")
