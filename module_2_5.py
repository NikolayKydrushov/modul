def get_matrix (n, m, value):
    matrix = []

    for i in range(n):
        empty = []
        matrix.append(empty)
        for j in range(m):
            empty.append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
print(result1)