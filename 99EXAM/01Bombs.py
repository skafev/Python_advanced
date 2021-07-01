from collections import deque

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120
datura_bombs_count = 0
cherry_bombs_count = 0
smoke_decoy_bombs_count = 0
filled_pouch = False
bombs_effects = deque([int(x) for x in input().split(", ")])
bombs_casings = [int(x) for x in input().split(", ")]

while not filled_pouch:
    if len(bombs_effects) == 0 or len(bombs_casings) == 0:
        break
    current_be = bombs_effects.popleft()
    current_bs = bombs_casings.pop()
    if current_be + current_bs == DATURA_BOMBS:
        datura_bombs_count += 1
    elif current_be + current_bs == CHERRY_BOMBS:
        cherry_bombs_count += 1
    elif current_be + current_bs == SMOKE_DECOY_BOMBS:
        smoke_decoy_bombs_count += 1
    else:
        current_bs -= 5
        bombs_effects.insert(0, current_be)
        bombs_casings.append(current_bs)
    if datura_bombs_count >= 3 and cherry_bombs_count >= 3 and smoke_decoy_bombs_count >= 3:
        filled_pouch = True

if filled_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bombs_effects) > 0:
    print(f'Bomb Effects: {", ".join(map(str, bombs_effects))}', sep=", ")
else:
    print("Bomb Effects: empty")

if len(bombs_casings) > 0:
    print(f'Bomb Casings: {", ".join(map(str, bombs_casings))}', sep=", ")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs_count}")
print(f"Datura Bombs: {datura_bombs_count}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs_count}")
