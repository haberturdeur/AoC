image = []
algorithm = []
with open("data.txt") as f:
    algorithm = [(1 if i == "#" else 0) for i in f.readline()[:-1]]
    assert f.readline() == "\n"
    for e, line in enumerate(f):
        image.append("000")
        image[-1] += "".join([("1" if c == "#" else "0") for c in line[:-1]])
        image[-1] += "000"
        if e == 0:
            image.insert(0, "".join(["0" for i in range(len(image[-1]))]))
            image.insert(0, "".join(["0" for i in range(len(image[-1]))]))
            image.insert(0, "".join(["0" for i in range(len(image[-1]))]))
    image.append("".join(["0" for i in range(len(image[-1]))]))
    image.append("".join(["0" for i in range(len(image[-1]))]))
    image.append("".join(["0" for i in range(len(image[-1]))]))

    print("\n".join([str(i) for i in image]))
    
def get_binary(data, x, y):
    out = ""
    for _y in range(-1, 2):
        for _x in range(-1, 2):
            out += data[y+_y][x+_x]
    return int(out, 2)

def enhance(img):
    out = ["0" for _ in range(len(img))]
    out[0] = "0" * len(img[0])
    out[-1] = "0" * len(img[-1])
    # print(out, sep="\n")
    for y in range(1, len(img)-1):
        for x in range(1, len(img[0])-1):
            print(img[y][x], end="")
            out[y] += str(algorithm[get_binary(img, x, y)])
        out[y] += "0"
        print("")
    return out
    # for y in range(len(img)):
    #     out.append("")
    #     :
    #         img[-1] += str(out[y][x])
    
for i in range(2):
    image = enhance(image)
    print(len(image[0])*"-")
    print("\n".join([str(i) for i in image]))
    print(len(image[0])*"-")
    

count = 0
for i in image:
    count += i.count("1")

print(count)