def input_to_list(count):
    lines = []
    for _ in range(count):
        components = input().split()
        for component in components:
            lines.append(component)

    return lines


def set_of_list(value):
    result = set(value)
    for i in result:
        print(i)


n = int(input())
all_elements = input_to_list(n)
set_of_list(all_elements)
