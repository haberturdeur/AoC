with open("data.txt", "rt") as data:
    aim = 0
    depth = 0
    x = 0
    for line in data:
        if line[0] == "u":
            aim -= int(line[-2])
        elif line[0] == "d":
            aim += int(line[-2])
        elif line[0] == "f":
            x += int(line[-2])
            depth += aim*int(line[-2])

    print(x*depth)