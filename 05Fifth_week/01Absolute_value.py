def absolute_value_of_numbers(numbers):
    result = [abs(n) for n in numbers]
    return result


numbers = map(float, input().split())
print(absolute_value_of_numbers(numbers))
