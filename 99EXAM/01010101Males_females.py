from collections import deque

males = [int(x) for x in input().split(" ")]
females = deque([int(x) for x in input().split(" ")])
matches_count = 0


while True:
    if len(females) == 0 or len(males) == 0:
        break

    current_male = males.pop()
    current_female = females.popleft()

    if current_female <= 0:
        males.append(current_male)
        continue
    elif current_male <= 0:
        females.appendleft(current_female)
        continue
    if current_female % 25 == 0:
        if females:
            females.popleft()
            males.append(current_male)
        continue
    elif current_male % 25 == 0:
        if males:
            males.pop()
            females.appendleft(current_female)
        continue

    if current_male == current_female:
        matches_count += 1
        continue
    elif current_male != current_female:
        current_male -= 2
        males.append(current_male)

print(f"Matches: {matches_count}")
if not males:
    print("Males left: none")
else:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(map(str, females))}")
