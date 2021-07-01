from collections import deque

PAID_COMMAND = "Paid"
END_COMMAND = "End"

q = deque()

while True:
    command = input()
    if command == PAID_COMMAND:
        while q:
            print(q.popleft())
    elif command == END_COMMAND:
        print(f"{len(q)} people remaining.")
        break
    else:
        q.append(command)
