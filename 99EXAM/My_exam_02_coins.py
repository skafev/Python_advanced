import math


def make_matrix():
    matrix_size = int(input())
    matrix = []
    for _ in range(matrix_size):
        row = input().split()
        matrix.append(row)
    return matrix


matrix = make_matrix()


def find_the_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "P":
                return row, col


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


player = find_the_player(matrix)
player_row = player[0]
player_column = player[1]
coins = 0
path = []
while True:
    command = input()
    if command == "up":
        potential_row = int(player_row - 1)
        potential_col = int(player_column)
        if is_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] != "X":
                coins += int(matrix[potential_row][potential_col])
                player_row = potential_row
                player_column = potential_col
                path.append([potential_row, potential_col])
            else:
                coins = math.floor(coins * 0.5)
                print(f"Game over! You've collected {coins} coins.")
                print(f"Your path:")
                break
        else:
            coins = math.floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print(f"Your path:")
            break
    elif command == "down":
        potential_row = int(player_row + 1)
        potential_col = int(player_column)
        if is_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] != "X":
                coins += int(matrix[potential_row][potential_col])
                player_row = potential_row
                player_column = potential_col
                path.append([potential_row, potential_col])
            else:
                coins = math.floor(coins * 0.5)
                print(f"Game over! You've collected {coins} coins.")
                print(f"Your path:")
                break
        else:
            coins = math.floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print(f"Your path:")
            break
    elif command == "left":
        potential_row = int(player_row)
        potential_col = int(player_column - 1)
        if is_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] != "X":
                coins += int(matrix[potential_row][potential_col])
                player_row = potential_row
                player_column = potential_col
                path.append([potential_row, potential_col])
            else:
                coins = math.floor(coins * 0.5)
                print(f"Game over! You've collected {coins} coins.")
                print(f"Your path:")
                break
        else:
            coins = math.floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print(f"Your path:")
            break
    elif command == "right":
        potential_row = int(player_row)
        potential_col = int(player_column + 1)
        if is_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] != "X":
                coins += int(matrix[potential_row][potential_col])
                player_row = potential_row
                player_column = potential_col
                path.append([potential_row, potential_col])
            else:
                coins = math.floor(coins * 0.5)
                print(f"Game over! You've collected {coins} coins.")
                print(f"Your path:")
                break
        else:
            coins = math.floor(coins * 0.5)
            print(f"Game over! You've collected {coins} coins.")
            print(f"Your path:")
            break
    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        print("Your path:")
        break
print(*path, sep="\n")
