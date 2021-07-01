from collections import deque

quantity_of_food = int(input())

orders = list(map(int, input().split()))
q = deque()
print(max(orders))
for ch in orders:
    q.append(ch)

while len(q) > 0:
    current_order = q[0]
    if quantity_of_food >= current_order:
        quantity_of_food -= current_order
        q.popleft()
        if len(q) == 0:
            print("Orders complete")
    else:
        result = []
        while len(q):
            result.append(q.popleft())
        print(f"Orders left: {' '.join(map(str, result))}")
        break
