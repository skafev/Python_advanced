from collections import deque

START_COMMAND = "Start"
END_COMMAND = "End"

water_quantity = int(input())
names = deque()

while True:
    command = input()
    if command == START_COMMAND:
        break
    names.append(command)

while True:
    command = input()
    if command == END_COMMAND:
        print(f"{water_quantity} liters left")
        break
    elif command.startswith("refill"):
        new_command = command.split()
        quantity = int(new_command[1])
        water_quantity += quantity
    else:
        litters = int(command)
        if litters <= water_quantity:
            print(f"{names.popleft()} got water")
            water_quantity -= litters
        else:
            print(f"{names.popleft()} must wait")
