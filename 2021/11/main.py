

data = [
    [1, 4, 4, 3, 5, 8, 2, 1, 4, 8],
    [6, 5, 5, 3, 7, 3, 4, 8, 5, 1],
    [1, 4, 5, 1, 7, 4, 1, 2, 4, 6],
    [8, 8, 3, 5, 2, 1, 8, 8, 6, 4],
    [1, 6, 6, 2, 3, 1, 7, 2, 6, 2],
    [1, 7, 3, 1, 6, 5, 6, 6, 2, 3],
    [1, 1, 2, 8, 1, 7, 8, 3, 6, 7],
    [5, 8, 4, 2, 3, 5, 1, 6, 6, 5],
    [6, 6, 7, 7, 3, 2, 6, 8, 4, 3],
    [7, 3, 8, 1, 4, 3, 3, 2, 6, 7]]


# data = [
#     [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
#     [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
#     [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
#     [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
#     [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
#     [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
#     [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
#     [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
#     [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
#     [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]

test = [
    [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7]
    ],
    [
        [8, 8, 0, 7, 4, 7, 6, 5, 5, 5],
        [5, 0, 8, 9, 0, 8, 7, 0, 5, 4],
        [8, 5, 9, 7, 8, 8, 9, 6, 0, 8],
        [8, 4, 8, 5, 7, 6, 9, 6, 0, 0],
        [8, 7, 0, 0, 9, 0, 8, 8, 0, 0],
        [6, 6, 0, 0, 0, 8, 8, 9, 8, 9],
        [6, 8, 0, 0, 0, 0, 5, 9, 4, 3],
        [0, 0, 0, 0, 0, 0, 7, 4, 5, 6],
        [9, 0, 0, 0, 0, 0, 0, 8, 7, 6],
        [8, 7, 0, 0, 0, 0, 6, 8, 4, 8]
    ],
    [
        [0, 0, 5, 0, 9, 0, 0, 8, 6, 6],
        [8, 5, 0, 0, 8, 0, 0, 5, 7, 5],
        [9, 9, 0, 0, 0, 0, 0, 0, 3, 9],
        [9, 7, 0, 0, 0, 0, 0, 0, 4, 1],
        [9, 9, 3, 5, 0, 8, 0, 0, 6, 3],
        [7, 7, 1, 2, 3, 0, 0, 0, 0, 0],
        [7, 9, 1, 1, 2, 5, 0, 0, 0, 9],
        [2, 2, 1, 1, 1, 3, 0, 0, 0, 0],
        [0, 4, 2, 1, 1, 2, 5, 0, 0, 0],
        [0, 0, 2, 1, 1, 1, 9, 0, 0, 0]
    ]
]

flashes = 0


def print_matrix(matrix):
    print("[")
    for line in matrix:
        print(f"{line},")
    print("]")


def around(x, y, matrix):
    out = []
    if x < len(matrix[y]) - 1:
        out.append((x+1, y))
    if y < len(matrix) - 1:
        out.append((x, y+1))
    if x > 0:
        out.append((x-1, y))
    if y > 0:
        out.append((x, y-1))

    if x > 0 and y > 0:
        out.append((x-1, y-1))
    if x > 0 and y < len(matrix)-1:
        out.append((x-1, y+1))
    if x < len(matrix[y]) - 1 and y < len(matrix)-1:
        out.append((x+1, y+1))
    if x < len(matrix[y]) - 1 and y > 0:
        out.append((x+1, y-1))
    return out


# test = [[0,0],[0,0],[0,0]]

# for x, y in around(1,1, test):
#     test[y][x] += 1
# print(test)


def run_point(x, y, matrix):
    global flashes
    flashes += 1
    # print_matrix(matrix)
    matrix[y][x] = -1
    for _x, _y in around(x, y, matrix):
        if matrix[_y][_x] != -1:
            matrix[_y][_x] += 1
            if matrix[_y][_x] > 9:
                run_point(_x, _y, matrix)


def step(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] != -1:
                matrix[y][x] += 1
            if matrix[y][x] > 9:
                run_point(x, y, matrix)

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == -1:
                matrix[y][x] = 0


def diff(a, b):
    out = [i[:] for i in a]
    for y in range(len(a)):
        for x in range(len(a[y])):
            out[y][x] -= b[y][x]
    return out

def check_all(matrix):
    for line in matrix:
        for x in line:
            if x != 0:
                return False
    return True

# print_matrix(data)

# step(data)
# print_matrix(data)
# print_matrix(diff(data, test[0]))
# assert test[0] == data
# step(data)
# print_matrix(data)
# assert test[1] == data
# step(data)
# print_matrix(data)
# assert test[2] == data

for i in range(1, 1000):
    step(data)
    if check_all(data):
        print(i)
        break

print(flashes)
