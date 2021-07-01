def get_grades(count):
    students = {}
    for i in range(count):
        students_line = input()
        (student, grade) = students_line.split()
        if student not in students:
            students[student] = []
        students[student].append(float(grade))
    return students


def get_average(values):
    total = sum(values) / len(values)
    return total


count_of_students = int(input())

for k, v in get_grades(count_of_students).items():
    all_grades = ' '.join(map(lambda x: f"{x:.2f}", v))
    average = get_average(v)
    print(f"{k} -> {all_grades} (avg: {average:.2f})")
