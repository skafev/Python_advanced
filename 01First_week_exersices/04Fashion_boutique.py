clothes = list(map(int, input().split()))
rack_capacity = int(input())
racks = 0
volume = 0

while len(clothes) > 0:
    current_cloth = clothes.pop()
    volume += current_cloth
    if volume > rack_capacity:
        racks += 1
        volume = 0
        clothes.append(current_cloth)

if volume > 0:
    racks += 1

print(racks)
