n = list(map(int, input().split()))
numbers = []

for i in n:
    numbers.append(i)

while len(numbers) > 0:
    print(numbers.pop(), end=" ")
