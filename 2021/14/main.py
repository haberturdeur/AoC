

original = "NCOPHKVONVPNSKSHBNPF"
# original = "NNCB"

data = {}
for k in range(len(original)-1):
    tmp = original[k:k+2]
    data.setdefault(tmp, 0)
    data[tmp] += 1

combinations = {}

tests = ["NNCB",
        "NCNBCHB",
        "NBCCNBBBCBHCB",
        "NBBBCNCCNBBNBNBBCHBHHBCHB",
        "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"]

testing = []

for test in tests:
    out = {}
    for k in range(len(test)-1):
        tmp = test[k:k+2]
        out.setdefault(tmp, 0)
        out[tmp] += 1
    testing.append(out)

print(testing)


with open("data.txt") as f:
    for line in f:
        combinations[str(line[:2])] = line[6]

for i in range(1, 41):
    new = {}
    for k, v in data.items():
        tmp = combinations[k]
        new.setdefault(k[0]+tmp, 0)
        new.setdefault(tmp+k[1], 0)
        new[k[0]+tmp] += v
        new[tmp+k[1]] += v

    data = new
    # for k, v in new.items():
    #     data.setdefault(k, 0)
    #     data[k] += v
    #     print(data[k], testing[i+1][k])
    # print(new)
    # print(i)

counts = {}

for k,v in data.items():
    counts.setdefault(k[0], 0)
    counts.setdefault(k[1], 0)
    counts[k[0]] += v
    counts[k[1]] += v

for k, v in counts.items():
    counts[k] = (v+1) // 2

print("B:", counts["B"])
print("H:", counts["H"])

print(max(counts.values()) - min(counts.values()))
