countries = input().split(", ")
capitals = input().split(", ")
result = {x: y for x, y in tuple(zip(countries, capitals))}
[print(f"{x} -> {y}") for x, y in result.items()]
