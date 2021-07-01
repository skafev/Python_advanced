import itertools

# def name_combination(names, number, combination=[]):
#     if len(combination) == number:
#         print(", ".join(combination))
#         return
#
#     for i in range(len(names)):
#         name = names[i]
#         combination.append(name)
#         name_combination(names[i + 1:], number, combination)
#         combination.pop()


names = input().split(", ")
number_of_chairs = int(input())
# name_combination(names, number_of_chairs)

result = itertools.combinations(names, number_of_chairs)
[print(', '.join(x)) for x in result]