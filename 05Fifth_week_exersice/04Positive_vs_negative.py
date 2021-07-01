def negative_numbers_of_list(numbers):
    negative_numbers = [n for n in numbers if n < 0]
    return negative_numbers


def positive_numbers_of_list(numbers):
    positive_numbers = [n for n in numbers if n >= 0]
    return positive_numbers


numbers = [int(x) for x in input().split()]
print(sum(negative_numbers_of_list(numbers)))
print(sum(positive_numbers_of_list(numbers)))

if abs(sum(negative_numbers_of_list(numbers))) > sum(positive_numbers_of_list(numbers)):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
