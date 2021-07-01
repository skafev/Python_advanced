from collections import deque

END_COMMAND = 'END'
GREEN_COMMAND = 'green'
green_light_duration = int(input())
free_window = int(input())
cars = deque()
passed_cars = 0
car_check = ""

while True:
    command = input()
    if command == END_COMMAND:
        break

    if command == GREEN_COMMAND:
        if free_window > 0:
            extra_time = free_window
        else:
            extra_time = -1
        green_light_countdown = green_light_duration
        for i in range(len(cars)):
            if len(cars) > 0 and extra_time == 0:
                break
            car = cars.popleft()
            if green_light_countdown > 0:
                for ch in car:
                    green_light_countdown -= 1
                    if green_light_countdown == 0:
                        green_light_countdown += extra_time
                        extra_time = 0
                    elif green_light_countdown < 0:
                        print("A crash happened!")
                        print(f"{car} was hit at {ch}.")
                        quit()

                    car_check += ch
                    if car == car_check:
                        passed_cars += 1
                        car_check = ""
                        if len(cars) == 0:
                            green_light_countdown = green_light_duration

    else:
        cars.append(command)

print('Everyone is safe.')
print(f"{passed_cars} total cars passed the crossroads.")
