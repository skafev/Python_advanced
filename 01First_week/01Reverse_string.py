text = input()

stack = []
result = ""

for ch in text:
    stack.append(ch)

while stack:
    result += stack.pop()

print(result)