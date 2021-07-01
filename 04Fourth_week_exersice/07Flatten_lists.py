text = input().split("|")
data = [el for i in range(len(text))[::-1] for el in text[i].split()]
print(*data)
