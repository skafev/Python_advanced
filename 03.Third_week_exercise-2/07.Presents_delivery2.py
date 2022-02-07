def make_matrix():
    matrix = []
    size_of_matrix = int(input())
    for _ in range(size_of_matrix):
        row = input().split()
        matrix.append(row)

    return matrix


def search_in_matrix(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def search_in_matrix_for_nice_kids(matrix, search):
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


def print_matrix():
    print('\n'.join([' '.join(row) for row in matrix]))


count_of_presents = int(input())
matrix = make_matrix()
row, col = search_in_matrix(matrix, "S")
present_received = 0
nice_kids = search_in_matrix_for_nice_kids(matrix, "V")
nice_kids_presents = 0
while True:
    if count_of_presents == 0:
        break
    command = input()
    if command == "Christmas morning":
        break
    if command == 'up':
        if is_valid(row - 1, col):
            if matrix[row - 1][col] == "V":
                present_received += 1
                nice_kids -= 1
                nice_kids_presents += 1
                count_of_presents -= 1
            elif matrix[row - 1][col] == "C":
                if is_valid(row - 2, col):
                    if matrix[row - 2][col] == "V":
                        if count_of_presents > 0:
                            nice_kids -= 1
                            nice_kids_presents += 1
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 2][col] = "-"
                    elif matrix[row - 2][col] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 2][col] = "-"
                if is_valid(row - 1, col + 1):
                    if matrix[row - 1][col + 1] == "V":
                        if count_of_presents > 0:
                            nice_kids -= 1
                            nice_kids_presents += 1
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 1][col + 1] = "-"
                    elif matrix[row - 1][col + 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 1][col + 1] = "-"
                if is_valid(row - 1, col - 1):
                    if matrix[row - 1][col - 1] == "V":
                        if count_of_presents > 0:
                            nice_kids -= 1
                            nice_kids_presents += 1
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 1][col - 1] = "-"
                    elif matrix[row - 1][col - 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 1][col - 1] = "-"
            matrix[row][col] = "-"
            matrix[row - 1][col] = "S"
            row = row - 1
    elif command == "down":
        if is_valid(row + 1, col):
            if matrix[row + 1][col] == "V":
                present_received += 1
                nice_kids -= 1
                nice_kids_presents += 1
                count_of_presents -= 1
            elif matrix[row + 1][col] == "C":
                if is_valid(row + 2, col):
                    if matrix[row + 2][col] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row + 2][col] = "-"
                    elif matrix[row + 2][col] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 2][col] = "-"
                if is_valid(row + 1, col + 1):
                    if matrix[row + 1][col + 1] == "V":
                        if count_of_presents > 0:
                            nice_kids -= 1
                            nice_kids_presents += 1
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 1][col + 1] = "-"
                    elif matrix[row + 1][col + 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 1][col + 1] = "-"

                if is_valid(row + 1, col - 1):
                    if matrix[row + 1][col - 1] == "V":
                        if count_of_presents > 0:
                            nice_kids -= 1
                            nice_kids_presents += 1
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 1][col - 1] = "-"
                    elif matrix[row + 1][col - 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 1][col - 1] = "-"
            matrix[row][col] = "-"
            matrix[row + 1][col] = "S"
            row = row + 1
    elif command == "left":
        if is_valid(row, col - 1):
            if matrix[row][col - 1] == "V":
                present_received += 1
                nice_kids -= 1
                nice_kids_presents += 1
                count_of_presents -= 1
            elif matrix[row][col - 1] == "C":
                if is_valid(row, col - 2):
                    if matrix[row][col - 2] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row][col - 2] = "-"
                    elif matrix[row][col - 2] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row][col - 2] = "-"
                if is_valid(row + 1, col - 1):
                    if matrix[row + 1][col - 1] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row + 1][col - 1] = "-"
                    elif matrix[row + 1][col - 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 1][col - 1] = "-"
                if is_valid(row - 1, col - 1):
                    if matrix[row - 1][col - 1] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row - 1][col - 1] = "-"
                    elif matrix[row - 1][col - 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 1][col - 1] = "-"
            matrix[row][col] = "-"
            matrix[row][col - 1] = "S"
            col = col - 1
    elif command == "right":
        if is_valid(row, col + 1):
            if matrix[row][col + 1] == "V":
                present_received += 1
                nice_kids -= 1
                nice_kids_presents += 1
                count_of_presents -= 1
            elif matrix[row][col + 1] == "C":
                if is_valid(row, col + 2):
                    if matrix[row][col + 2] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row][col + 2] = "-"
                    elif matrix[row][col + 2] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row][col + 2] = "-"
                if is_valid(row - 1, col + 1):
                    if matrix[row - 1][col + 1] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row - 1][col + 1] = "-"
                    elif matrix[row - 1][col + 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row - 1][col + 1] = "-"
                if is_valid(row + 1, col + 1):
                    if matrix[row + 1][col + 1] == "V":
                        if count_of_presents > 0:
                            present_received += 1
                            nice_kids -= 1
                            nice_kids_presents += 1
                            count_of_presents -= 1
                            matrix[row + 1][col + 1] = "-"
                    elif matrix[row + 1][col + 1] != "-":
                        if count_of_presents > 0:
                            present_received += 1
                            count_of_presents -= 1
                            matrix[row + 1][col + 1] = "-"
            matrix[row][col] = "-"
            matrix[row][col + 1] = "S"
            col = col + 1
if count_of_presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")
print_matrix()
if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_presents} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")
