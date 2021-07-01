from collections import deque

fireworks = deque([int(x) for x in input().strip().split(", ")])
explosives = [int(x) for x in input().strip().split(", ")]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
new_fireworks = deque([])
new_explosives = []
for f in fireworks:
    if f > 0:
        new_fireworks.append(f)
for e in explosives:
    if e > 0:
        new_explosives.append(e)
while True:
    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        print(f"Congrats! You made the perfect firework show!")
        break
    if len(new_explosives) == 0 or len(new_fireworks) == 0:
        print(f"Sorry. You can’t make the perfect firework show.")
        break
    current_firework = new_fireworks.popleft()
    current_explosive = new_explosives.pop()
    if current_firework < 0:
        new_explosives.append(current_explosive)
        continue
    sum_of_power = current_firework + current_explosive
    if sum_of_power % 3 == 0 and sum_of_power % 5 != 0:
        palm_fireworks += 1
    elif sum_of_power % 5 == 0 and sum_of_power % 3 != 0:
        willow_fireworks += 1
    elif sum_of_power % 5 == 0 and sum_of_power % 3 == 0:
        crossette_fireworks += 1
    else:
        current_firework -= 1
        new_fireworks.append(current_firework)
        new_explosives.append(current_explosive)

if new_fireworks:
    print(f"Firework Effects left: {', '.join(map(str, new_fireworks))}")
if new_explosives:
    print(f"Explosive Power left: {', '.join(map(str, new_explosives))}")
print(f'Palm Fireworks: {palm_fireworks}')
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
