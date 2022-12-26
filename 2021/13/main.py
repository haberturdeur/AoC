

folds = ["x=655",
         "y=447",
         "x=327",
         "y=223",
         "x=163",
         "y=111",
         "x=81",
         "y=55",
         "x=40",
         "y=27",
         "y=13",
         "y=6"]
data = set()
with open("data.txt") as f:
    for line in f:
        tmp = line.split(",")
        data.add((int(tmp[0]), int(tmp[1])))

def fold_x(x: int, data):
    out = set()
    for i in data:
        if i[0] > x:
            out.add((2*x-i[0], i[1]))
        else:
            out.add(i)
    return out

def fold_y(y: int, data):
    out = set()
    for i in data:
        if i[1] > y:
            out.add((i[0], 2*y-i[1]))
        else:
            out.add(i)
    return out

print(len(data))


for i in folds:
    if i[0] == "x":
        data = fold_x(int(i[2:]), data)
    else:
        data = fold_y(int(i[2:]), data)

print(len(data))

y, x = 0, 0

for i in data:
    if x < i[0]:
        x = i[0]
    if y < i[1]:
        y = i[1]

out = [[" " for _ in range(x+1)] for _ in range(y+1)]


for i in data:
    out[i[1]][i[0]] = "#"

for line in out:
    print("".join(line))
