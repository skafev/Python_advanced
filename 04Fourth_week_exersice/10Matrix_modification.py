END_COMMAND = "END"
ADD_COMMAND = "Add"
SUBTRACT_COMMAND = "Subtract"
row = int(input())
matrix = [[i for i in list(map(int, input().split()))] for x in range(row)]

while True:
    command = input()
    if command == END_COMMAND:
        break

    coordinates, r, c, value = command.split()
    r = int(r)
    c = int(c)
    if int(r) >= row or int(r) < 0 or int(c) >= len(matrix) or int(c) < 0:
        print("Invalid coordinates")
        continue

    if coordinates == ADD_COMMAND:
        matrix[r][c] += int(value)
    elif coordinates == SUBTRACT_COMMAND:
        matrix[r][c] -= int(value)

for m in matrix:
    print(' '.join(map(str, m)))
