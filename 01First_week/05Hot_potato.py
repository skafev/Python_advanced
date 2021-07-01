from collections import deque

name = input().split()
n = int(input())
q = deque(name)
counter = 0

while len(q) > 1:
    current_name = q.popleft()
    counter += 1
    if counter == n:
        print(f"Removed {current_name}")
        counter = 0
    else:
        q.append(current_name)

print(f"Last is {q.popleft()}")
