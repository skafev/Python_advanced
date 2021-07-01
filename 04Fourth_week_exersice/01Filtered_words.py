words = input().split()
filter_word = [word for word in words if len(word) % 2 == 0]

print(*filter_word, sep="\n")