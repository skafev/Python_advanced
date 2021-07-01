from collections import deque

bullet_cost = int(input())
size_of_the_gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = input().split()
q = deque()

for lock in locks:
    q.append(lock)

intelligence = int(input())
bullet_used = 0
index_of_gun_barrel = 0

while len(bullets) > 0:
    if len(q) > 0:
        for i in range(size_of_the_gun_barrel):
            if len(q) <= 0:
                break
            current_lock = int(q[0])
            if len(bullets) <= 0:
                break
            current_bullet = int(bullets[-1])
            if current_bullet <= current_lock:
                print("Bang!")
                q.popleft()
            else:
                print("Ping!")
            bullets.pop()
            bullet_used += 1
            index_of_gun_barrel += 1
            if index_of_gun_barrel == size_of_the_gun_barrel:
                if len(bullets) > 0:
                    print("Reloading!")
                index_of_gun_barrel = 0
    else:
        break

total = bullet_used * bullet_cost
if len(q) == 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - total}")
else:
    print(f"Couldn't get through. Locks left: {len(q)}")
