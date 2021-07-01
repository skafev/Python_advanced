from collections import deque

number_of_stops = int(input())
petrol_stations = deque([])

for stops in range(number_of_stops):
    petrol_stations.append([el for el in input().split()])

for start_station in range(number_of_stops):
    tank = 0
    is_valid = True
    for current_rotation in range(number_of_stops):
        tank += int(petrol_stations[current_rotation][0]) - int(petrol_stations[current_rotation][1])
        if tank < 0:
            petrol_stations.append(petrol_stations.popleft())
            is_valid = False
            break

    if is_valid:
        print(start_station)
        break
