start = int(input())
stop = int(input())


def filtered_numbers(x):
    return any(x % i == 0 for i in range(2, 10))


result = [x for x in range(start, stop + 1) if filtered_numbers(x)]
print(result)