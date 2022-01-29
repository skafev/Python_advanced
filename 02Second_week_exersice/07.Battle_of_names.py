number = int(input())
names = []
for _ in range(number):
    x = input()
    names.append(x)


odd_numbers = set()
even_numbers = set()
for name in names:
    iterations = names.index(name) + 1
    i = 0
    total_number = 0
    while i != len(name):
        num = ord(name[i])
        i += 1
        total_number += num
    result = total_number // iterations
    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)

if sum(odd_numbers) == sum(even_numbers):
    print(', '.join(map(str, odd_numbers.union(even_numbers))))
elif sum(odd_numbers) > sum(even_numbers):
    print(', '.join(map(str, odd_numbers.difference(even_numbers))))
else:
    print(', '.join(map(str, odd_numbers.symmetric_difference(even_numbers))))
