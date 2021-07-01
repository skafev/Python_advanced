expression = input()

stack = []

for i in range(len(expression)):
    symbol = expression[i]
    if symbol == "(":
        stack.append(i)
    elif symbol == ")":
        j = stack.pop()
        print(expression[j:i + 1])
