def first_set(n):
    first_set = set()
    for i in range(n):
        first = int(input())
        first_set.add(first)

    return first_set


def second_set(m):
    second_set = set()
    for j in range(m):
        second = int(input())
        second_set.add(second)

    return second_set


def compare_set(one, two):
    result = (one.intersection(two))

    return result


def print_result(value):
    for v in value:
        print(v)


n, m = list(map(int, input().split()))
print_result(compare_set(first_set(n), second_set(m)))
