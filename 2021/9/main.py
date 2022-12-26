from typing import Set, Tuple

def is_minimum(array, x, y):
    curr = array[y][x]
    return ((array[y][x-1] > curr if x != 0 else True)
            and (array[y][x+1] > curr if x != len(array[y]) - 1 else True)
            and (array[y-1][x] > curr if y != 0 else True)
            and (array[y+1][x] > curr if y != len(array) - 1 else True))


def check_adjacent(array, basin: Set[Tuple[int, int]], x, y):
    curr = array[y][x]
    print(x, y)
    if x != 0 and curr < array[y][x-1] and array[y][x-1] != 9:
        basin.add((x-1, y))
        check_adjacent(array, basin, x-1, y)
    if y != 0 and curr < array[y-1][x] and array[y-1][x] != 9:
        basin.add((x, y-1))
        check_adjacent(array, basin, x, y-1)
    if x != len(array[y]) - 1 and curr < array[y][x+1] and array[y][x+1] != 9:
        basin.add((x+1, y))
        check_adjacent(array, basin, x+1, y)
    if y != len(array) - 1 and curr < array[y+1][x] and array[y+1][x] != 9:
        basin.add((x, y+1))
        check_adjacent(array, basin, x, y+1)

data = []
with open("milan.txt") as f:
    for line in f:
        data.append(list(map(int, line[:-1])))

basins = []

for y in range(len(data)):
    for x in range(len(data[y])):
        if is_minimum(data, x, y):
            temp = {(x, y)}
            check_adjacent(data, temp, x, y)
            basins.append(temp)
            # print(temp)

lengths = []
for b in basins:
    lengths.append(len(b))
    
for l in sorted(lengths):
    print(l)
out = 1

for i in range(3):
    m = max(basins, key=len)
    out *= len(m)
    basins.remove(m)

print(out)