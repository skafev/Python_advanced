def make_matrix():
    matrix = []
    size = int(input())
    for row_index in range(size):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix


matrix = make_matrix()
result = [[x for x in row if x % 2 == 0] for row in matrix]
print(result)
