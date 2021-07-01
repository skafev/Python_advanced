def find_missing(lst, biggest, smallest):
    return [x for x in range(smallest, biggest + 1)
            if x not in lst]


def numbers_searching(*args):
    biggest_number = max(args)
    smallest_number = min(args)
    duplicate_nums = []

    for n in range(smallest_number, biggest_number + 1):
        res = args.count(n)
        if res > 1:
            duplicate_nums.append(n)
    missing = find_missing(args, biggest_number, smallest_number)
    return [*missing, sorted(duplicate_nums)]

