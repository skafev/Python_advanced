ODD_COMMAND = "Odd"
EVEN_COMMAND = "Even"


def odd_numbers_of_list(nums):
    odd_numbers = [n for n in nums if n % 2 == 1]
    return odd_numbers


def even_numbers_of_list(nums):
    even_numbers = [n for n in nums if n % 2 == 0]
    return even_numbers


command = input()
numbers = [int(x) for x in input().split()]

if command == ODD_COMMAND:
    print(sum(odd_numbers_of_list(numbers) * len(numbers)))
elif command == EVEN_COMMAND:
    print(sum(even_numbers_of_list(numbers) * len(numbers)))
