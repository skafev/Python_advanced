def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def unique_name(names):
    result = set(names)
    for i in result:
        print(i)


n = int(input())
all_names = input_to_list(n)
unique_name(all_names)
