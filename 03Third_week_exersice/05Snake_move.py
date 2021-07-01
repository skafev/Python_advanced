from collections import deque

rows_count, columns_count = map(int, input().split(" "))


def make_matrix():
    matrix = []
    for _ in range(rows_count):
        matrix.append([0 for _ in range(columns_count)])

    return matrix


matrix = make_matrix()
snake = input()

q = deque()
for ch in snake:
    q.append([ch])

for r in range(rows_count):
    for c in range(columns_count):
        matrix[r].pop(c)
        sting_to_add = q.popleft()
        matrix[r].insert(c, sting_to_add)
        q.append(sting_to_add)
    if r % 2 != 0:
        matrix[r] = list(reversed(matrix[r]))

result = ""
for m in matrix:
    for el in m:
        result += ("".join(str(x) for x in el))
    print(result)
    result = ""
