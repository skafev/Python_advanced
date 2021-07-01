def make_matrix():
    matrix_size = int(input())
    matrix = []
    for row_index in range(matrix_size):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    return matrix


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


matrix = make_matrix()
number_of_bombs = input().split(" ")
while len(number_of_bombs) > 0:
    try:
        current_bomb = number_of_bombs[0]
        row_one = int(current_bomb[0])
        column_one = int(current_bomb[2])
    except IndexError:
        break
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r == int(row_one) and c == int(column_one):
                current_row_data = matrix[r][c]
                row = [-1, -1, -1, 0, 0, 1, 1, 1]
                col = [1, 0, -1, -1, 1, 1, 0, -1]
                for index in range(len(row)):
                    bomb_row = r + row[index]
                    bomb_column = c + col[index]
                    if current_row_data > 0:
                        if is_valid(bomb_row, bomb_column):
                            bomb_to_explode = matrix[bomb_row][bomb_column]
                            if bomb_to_explode > 0:
                                matrix[bomb_row][bomb_column] -= current_row_data
                if current_row_data > 0:
                    matrix[r][c] = 0
                number_of_bombs.remove(current_bomb)
                break

alive_cells = 0
sum_of_alive_cells = 0
for data in matrix:
    for i in data:
        if i > 0:
            alive_cells += 1
            sum_of_alive_cells += i

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
for m in matrix:
    print(" ".join(map(str, m)))
