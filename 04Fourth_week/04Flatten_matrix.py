matrix = [[i for i in list(map(int, input().split(", ")))] for x in range(int(input()))]
flatten_matrix = [num for sublist in matrix for num in sublist]
print(flatten_matrix)
