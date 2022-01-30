def make_matrix(num):
    matrix_maker = []
    for _ in range(num):
        i = [x for x in input()]
        matrix_maker.append(i)
    return matrix_maker


def search_for_a_knight(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


def move():
    pass


n = int(input())
matrix = make_matrix(n)
