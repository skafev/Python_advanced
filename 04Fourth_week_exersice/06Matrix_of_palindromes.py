rows, columns = list(map(int, input().split()))
result = [[f"{chr(97 + r)}{chr(97 + c + r)}{chr(97 + r)}" for c in range(columns)] for r in range(rows)]

print(*[" ".join(res) for res in result], sep='\n')
