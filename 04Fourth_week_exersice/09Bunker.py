categories = {category: [] for category in input().split(", ")}
n = int(input())
quality = 0
quantity = 0

for _ in range(n):
    cat, items, data = input().split(" - ")
    data_info = data.split(";")
    quantity_info = data_info[0].split(":")
    quality_info = data_info[1].split(":")
    quantity += int(quantity_info[1])
    quality += int(quality_info[1])

    categories[cat].append(items)

print(f"Count of items: {quantity}")
print(f"Average quality: {quality/(len(categories)):.2f}")
[print(f"{k} -> {', '.join(v)}") for k, v in categories.items()]
