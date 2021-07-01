vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)
text = input()

result = [ch for ch in text if ch not in vowels]
print("".join(result))
