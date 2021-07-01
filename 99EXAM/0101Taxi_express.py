from collections import deque

customers = deque(list(map(int, input().split(", "))))
taxis = list(map(int, input().split(", ")))
total_time = sum(customers)

while len(customers) > 0:
    if len(taxis) > 0:
        current_customer_time = customers.popleft()
        current_taxi_fuel = taxis.pop()
        if current_taxi_fuel >= current_customer_time:
            continue
        else:
            customers.insert(0, current_customer_time)
    else:
        break

if len(taxis) == 0 and len(customers) > 0:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str, customers))}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
