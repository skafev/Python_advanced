ALICE = "A"
RABBIT_HOLE = "R"


def make_matrix():
    matrix = []
    matrix_size = int(input())
    for row_index in range(matrix_size):
        row = list(input().split())
        matrix.append(row)
    return matrix


def search_in_matrix(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def is_valid(r, c):
    if 0 <= r < len(territory) and 0 <= c < len(territory):
        return True
    return False


def move(dy, dx):
    global current_position, game_over, tea_bags_count
    y, x = current_position
    territory[y][x] = '*'
    new_y = y + dy
    new_x = x + dx
    if not is_valid(new_y, new_x):
        print("Alice didn't make it to the tea party.")
        game_over = True
        return
    if territory[new_y][new_x].isdigit():
        tea_bags_count += int(territory[new_y][new_x])
        if tea_bags_count >= 10:
            territory[new_y][new_x] = '*'
            print("She did it! She went to the party.")
            game_over = True
            return
    if territory[new_y][new_x] == "R":
        territory[new_y][new_x] = '*'
        print("Alice didn't make it to the tea party.")
        game_over = True
        return
    territory[new_y][new_x] = '*'
    current_position = (new_y, new_x)


def print_territory():
    print('\n'.join([' '.join(row) for row in territory]))


operations = {
    'up': lambda: move(-1, 0),
    'down': lambda: move(1, 0),
    'left': lambda: move(0, -1),
    'right': lambda: move(0, 1),
}

territory = make_matrix()
current_position = search_in_matrix(territory, ALICE)
tea_bags_count = 0
game_over = False

while not game_over:
    command = input()
    move_fn = operations[command]
    move_fn()

print_territory()
