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


def when_cookie_found(row, col, command):
    global nice_kids_that_got_presents, presents_count
    if command == 'up':
        if matrix[row - 2][col] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row - 2][col] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row - 2][col] = "-"
        if matrix[row - 1][col - 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row - 1][col - 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row - 1][col - 1] = "-"
        if matrix[row - 1][col + 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row - 1][col + 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row - 1][col + 1] = "-"
    elif command == "down":
        if matrix[row + 2][col] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row + 2][col] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row + 2][col] = "-"
        if matrix[row + 1][col + 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row + 1][col + 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row + 1][col + 1] = "-"
        if matrix[row + 1][col - 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row + 1][col - 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row + 1][col - 1] = "-"
    elif command == "left":
        if matrix[row][col - 2] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row][col - 2] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row][col - 2] = "-"
        if matrix[row + 1][col - 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row + 1][col - 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row + 1][col - 1] = "-"
        if matrix[row - 1][col - 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row - 1][col - 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row - 1][col - 1] = "-"
    elif command == "right":
        if matrix[row][col + 2] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row][col + 2] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row][col + 2] = "-"
        if matrix[row + 1][col + 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row + 1][col + 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row + 1][col + 1] = "-"
        if matrix[row - 1][col + 1] == "V":
            if presents_count > 0:
                nice_kids_that_got_presents += 1
                presents_count -= 1
        elif matrix[row - 1][col + 1] == "X":
            if presents_count > 0:
                presents_count -= 1
        matrix[row - 1][col + 1] = "-"


presents_count = int(input())
matrix = make_matrix()
row, col = search_in_matrix(matrix, "S")
count_of_nice_kids = search_in_matrix_for_nice_kids(matrix, "V")
nice_kids_that_got_presents = 0

while True:
    if presents_count == 0:
        break
    command = input()
    if command == "Christmas morning":
        break
    if command == "up":
        potential_position = matrix[row - 1][col]
        if is_valid(row - 1, col):
            if potential_position == "V":
                if presents_count > 0:
                    nice_kids_that_got_presents += 1
                    presents_count -= 1
            elif potential_position == "C":
                when_cookie_found(row, col, command)
            matrix[row - 1][col] = "S"
            matrix[row][col] = "-"
            row = row - 1
    elif command == "down":
        potential_position = matrix[row + 1][col]
        if is_valid(row + 1, col):
            if potential_position == "V":
                if presents_count > 0:
                    nice_kids_that_got_presents += 1
                    presents_count -= 1
            elif potential_position == "C":
                when_cookie_found(row, col, command)
            matrix[row + 1][col] = "S"
            matrix[row][col] = "-"
            row = row + 1
    elif command == "left":
        potential_position = matrix[row][col - 1]
        if is_valid(row, col - 1):
            if potential_position == "V":
                if presents_count > 0:
                    nice_kids_that_got_presents += 1
                    presents_count -= 1
            elif potential_position == "C":
                when_cookie_found(row, col, command)
            matrix[row][col - 1] = "S"
            matrix[row][col] = "-"
            col = col - 1
    elif command == "right":
        potential_position = matrix[row][col + 1]
        if is_valid(row, col + 1):
            if potential_position == "V":
                if presents_count > 0:
                    nice_kids_that_got_presents += 1
                    presents_count -= 1
            elif potential_position == "C":
                when_cookie_found(row, col, command)
            matrix[row][col + 1] = "S"
            matrix[row][col] = "-"
            col = col + 1

nice_kids_presents = count_of_nice_kids - nice_kids_that_got_presents
if presents_count == 0 and nice_kids_presents > 0:
    print("Santa ran out of presents!")
print_matrix()
if nice_kids_presents == 0:
    print(f"Good job, Santa! {count_of_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_presents} nice kid/s.")
