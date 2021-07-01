def count_of_occurences(data):
    result = {}

    for ch in data:
        result[ch] = data.count(ch)

    for k, v in sorted(result.items()):
        print(f"{k}: {v} time/s")


text = input()
count_of_occurences(text)