rows_count, columns_count = map(int, input().split(" "))
END_COMMAND = "END"
SWAP_KEYWORD = "swap"


def make_matrix():
    matrix = []
    for row_index in range(rows_count):
        row = input().split()
        matrix.append(row)
    return matrix


matrix = make_matrix()

while True:
    command = input()
    if command == END_COMMAND:
        break
    data = command.split()
    if data[0] == SWAP_KEYWORD and len(data) == 5:
        row_one, col_one, row_two, col_two = [int(data[i]) for i in range(1, 5)]

        try:
            temp = matrix[row_one][col_one]
            matrix[row_one][col_one] = matrix[row_two][col_two]
            matrix[row_two][col_two] = temp
            for i in matrix:
                print(' '.join(i))
        except IndexError:
            print("Invalid input!")
    else:
        print("Invalid input!")
