def even_odd(*args):
    command = args[-1]
    if command == "even":
        return [x for x in args[0:-1] if x % 2 == 0]
    elif command == "odd":
        return [x for x in args[0:-1] if x % 2 == 1]

