def get_magic_triangle(number):
    triangle = [[1], [1, 1]]
    rows = 2
    while rows != number:
        new_row = []
        for r in range(rows):
            if r == 0:
                new_row.append(1)
            if r == rows - 1:
                new_row.append(1)
            else:
                nr = triangle[-1]
                if len(nr) == 2:
                    new_row.append(2)
                else:
                    new_row.append(nr[r] + nr[r + 1])
        triangle.append(new_row)
        rows += 1
    return triangle


get_magic_triangle(5)