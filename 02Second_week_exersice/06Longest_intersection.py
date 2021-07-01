n = int(input())

first_set = set()
second_set = set()
longest_intersection = []
for _ in range(n):
    first, second = input().split("-")
    start_range, end_range = list(map(int, first.split(",")))
    for i in range(start_range, end_range + 1):
        first_set.add(i)
    s_start_range, s_end_range = list(map(int, second.split(",")))
    for j in range(s_start_range, s_end_range + 1):
        second_set.add(j)

    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = list(current_intersection)
    first_set = set()
    second_set = set()

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
