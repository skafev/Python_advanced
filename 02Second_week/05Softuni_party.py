def input_to_list(count):
    lines = set()
    for _ in range(count):
        lines.add(input())

    return lines


def guest_who_didnt_arrived(all_guest):
    while True:
        command = input()
        if command == "END":
            break
        guest = command
        all_guest.remove(guest)
    not_arrived_guest = all_guest

    return not_arrived_guest


n = int(input())
reservations = input_to_list(n)
not_arrived = guest_who_didnt_arrived(reservations)

print(f"{len(not_arrived)}")

sorted_not_arrived = sorted(not_arrived)
for g in sorted_not_arrived:
    print(g)
