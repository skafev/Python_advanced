parentheses = input()
is_balanced = True
opening = []
mirror_parentheses = {"{": "}", "[": "]", "(": ")"}

for p in parentheses:
    if p in "([{":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        current_p = opening.pop()
        if not mirror_parentheses[current_p] == p:
            is_balanced = False
            break

if len(opening) > 0:
    is_balanced = False
if is_balanced:
    print('YES')
else:
    print('NO')
