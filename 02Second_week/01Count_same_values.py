def count_values(values):
    values_count = {}
    for value in values:
        if value not in values_count:
            values_count[value] = 0
        values_count[value] += 1
    return values_count


data = tuple(map(float, input().split()))
for (k, v) in count_values(data).items():
    print(f"{k} - {v} times")
