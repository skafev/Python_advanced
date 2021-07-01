def best_list_pureness(*args):
    lst = args[0]
    rotation = args[1]
    best_pureness = 0
    total = 0
    best_rotation = 0
    current_rotation = 0
    while rotation > -1:
        current_rotation += 1
        for index in range(len(lst)):
            current_pureness = lst[index] * index
            total += current_pureness
            if total > best_pureness:
                best_pureness = total
                best_rotation = current_rotation - 1
        total = 0
        last = lst.pop()
        lst.insert(0, last)
        rotation -= 1
    return f"Best pureness {best_pureness} after {best_rotation} rotations"

