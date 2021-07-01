from collections import deque

cups = input().split()
bottles = list(map(int, input().split()))
capacity_of_cups = deque()
wasted_water = 0

for c in cups:
    capacity_of_cups.append(c)

while True:
    if len(capacity_of_cups) <= 0 or len(bottles) <= 0:
        break

    current_bottle = bottles[-1]
    current_cup = int(capacity_of_cups[0])
    if current_bottle >= current_cup:
        wasted_water += current_bottle - current_cup
        bottles.pop()
        capacity_of_cups.popleft()
    else:
        current_cup -= current_bottle
        bottles.pop()
        while current_cup > 0:
            if len(bottles) > 0:
                current_bottle = bottles.pop()
                current_cup -= current_bottle
        capacity_of_cups.popleft()
        wasted_water += abs(current_cup)
result = []
if len(bottles) > 0:
    for b in bottles:
        result.append(b)
    print(f"Bottles: {' '.join(map(str, result))}")
else:
    print(f"Cups: {' '.join(map(str, capacity_of_cups))}")
print(f"Wasted litters of water: {wasted_water}")
