numbers = [int(x) for x in input().split(", ")]
index = int(input())

needed_number = numbers[index]
clock_cycles = 0  # ???
for i in range(len(numbers)):
    current_number = numbers[i]
    if i == index:
        continue
    if current_number < needed_number:
        clock_cycles += current_number
    elif current_number == needed_number:
        if i > index:
            continue
        clock_cycles += current_number

result = clock_cycles + needed_number
print(result)
