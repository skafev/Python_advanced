import itertools


# def char_combinations(text, current_index=0):
#     if len(text) == current_index:
#         print(''.join(text))
#         return
#
#     for i in range(current_index, len(text)):
#         text[current_index], text[i] = text[i], text[current_index]
#         char_combinations(text, current_index + 1)
#         text[current_index], text[i] = text[i], text[current_index]
#
#
info = list(input())
# char_combinations(info)

res = list(itertools.permutations(info))
[print(''.join(x)) for x in res]
