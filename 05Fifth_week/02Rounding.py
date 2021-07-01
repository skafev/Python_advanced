def round_numbers(numbers):
    result = [round(n) for n in numbers]
    return result


numbers = map(float, input().split())
print(round_numbers(numbers))
