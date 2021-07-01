END_COMMAND = "End"
names = input().split(", ")
heroes = {}

while True:
    command = input()
    if command == END_COMMAND:
        break
    name, item, cost = command.split("-")

    if not heroes.get(name):
        heroes[name] = {}
        heroes[name] = {item: int(cost)}
    if item not in heroes[name]:
        heroes[name].update({item: int(cost)})
for name in names:
    for k, v in heroes.items():
        if k == name:
            print(f"{k} -> Items: {len(v)}, Cost: {(sum(price for item, price in v.items()))}")
