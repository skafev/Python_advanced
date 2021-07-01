def unique_names(count):
    all_names = []

    for i in range(count):
        name = input()
        all_names.append(name)

    filter_names = set(all_names)
    for name in filter_names:
        print(name)


count_of_names = int(input())
unique_names(count_of_names)