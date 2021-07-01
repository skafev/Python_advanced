def min_number_of_list(numbers):
    return min(numbers)


def max_number_of_list(numbers):
    return max(numbers)


def sum_numbers_of_list(numbers):
    return sum(numbers)


numbers = [int(x) for x in input().split()]

print(f"The minimum number is {min_number_of_list(numbers)}")
print(f"The maximum number is {max_number_of_list(numbers)}")
print(f"The sum number is: {sum_numbers_of_list(numbers)}")
