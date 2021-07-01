def expressions(numbers, current_sum=0, exp=""):
    if not numbers:
        return [(exp, current_sum)]

    result_plus = expressions(numbers[1:], current_sum + numbers[0], f'{exp}+{numbers[0]}')
    result_minus = expressions(numbers[1:], current_sum - numbers[0], f'{exp}-{numbers[0]}')
    return result_plus + result_minus


numbers = list(map(int, input().split(", ")))
n = len(numbers)
print(*[f'{el[0]}={el[1]}' for el in expressions(numbers)], sep="\n")
