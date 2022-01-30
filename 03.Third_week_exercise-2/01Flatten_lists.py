matrix = [reversed(x.rstrip().lstrip().split(' ')) for x in input().split("|")]
result = []
for _ in matrix:
    for i in _:
        if i.isdigit():
            result.append(i)

print(*result.__reversed__())
