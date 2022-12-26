
def parse_value(data, pos):
    flag = False
    value = 0
    while pos < len(data):
        flag = data[pos] == "0"
        pos += 1
        for i in range(4):
            value = value << 1 | int(data[pos])
            pos += 1
        if flag:
            break
    return (pos, value)


data = []
packets = []
with open("tets.txt") as f:
    for line in f:
        for c in line:
            # data = (data << 4) | (int(c, base=16))
            for i in range(4):
                data.append(str(((int(c, base=16)) >> (3 - i)) & 1))
    
    while data[-1] == "0":
        data.pop()
    
    for a in data:
        print(a, end='')
    print("")
    print(len(data))

    pos = 0
    while pos < len(data):
        _version = int(''.join(data[pos:pos+3]), base=2)
        _type = int(''.join(data[pos+3:pos+6]), base=2)
        pos += 6
        if _type == 4:
            pos, value = parse_value(data, pos)
        else:
            
        
        print(_version, _type, value)
