from collections import deque


def stock_availability(lst, command, *args):
    lst = deque(lst)
    command = command
    rest = args
    if command == "delivery":
        if len(rest) > 1:
            for x in rest:
                lst.append(x)
    elif command == "sell":
        if not rest:
            lst.popleft()
        for x in rest:
            if str(x).isdigit():
                for _ in range(x):
                    lst.popleft()
            else:
                for stock in rest:
                    if stock in lst:
                        while stock in lst:
                            lst.remove(stock)
    result = []
    for res in lst:
        result.append(res)
    return result

