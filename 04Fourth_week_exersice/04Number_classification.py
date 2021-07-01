numbers = list(map(float, input().split(", ")))

positive = []
negative = []
odd = []
even = []

for number in numbers:
    if number >= 0:
        positive.append(int(number))
    if number < 0:
        negative.append(int(number))
    if number % 2 == 0:
        even.append(int(number))
    if not number % 2 == 0:
        odd.append(int(number))

print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")
