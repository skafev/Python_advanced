queries = int(input())
numbers = []

for i in range(queries):
    command = input()
    if command.startswith("1"):
        new_command = command.split()
        push = new_command[1]
        numbers.append(int(push))
    elif command == "2":
        if len(numbers) > 0:
            numbers.pop()
    elif command == "3":
        if len(numbers) > 0:
            print(max(numbers))
    else:
        if len(numbers) > 0:
            print(min(numbers))

result = []
for i in range(len(numbers)):
    result.append(numbers.pop())
print(', '.join(map(str, result)))
