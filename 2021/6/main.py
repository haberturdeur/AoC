

offsets = {}
for i in range(7):
    offsets[i] = 0
data = [1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1, 4, 1, 5, 1, 3, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 5, 2, 5, 1, 1, 2, 1, 1, 1, 1, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 5, 4, 1, 1, 1, 1, 1, 5, 1, 2, 4, 1, 1, 1, 1, 1, 3, 3, 2, 1, 1, 4, 1, 1, 5, 5, 1, 1, 1, 1, 1, 2, 5, 1, 4, 1, 1, 1, 1, 1, 1, 2, 1, 1, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 1, 1, 3, 1, 3, 1, 4, 1, 5, 4, 1, 1, 2, 1, 1, 5, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 5, 4, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 2, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 1, 2, 1, 1, 4, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 4, 1, 5, 1, 1, 1, 4, 5, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 1, 2, 1, 1, 2, 4, 1, 1, 2, 1, 5, 5, 3]

carry1 = [0, 0, 0, 0, 0, 0, 0, 0]
carry2 = [0, 0, 0, 0, 0, 0, 0, 0]
count = 0

for i in data:
    offsets.setdefault(int(i), 0)
    offsets[int(i)] += 1


def run(remining):
    for j in range(len(data)):
        if data[j] == 0:
            data[j] = 6
            data.append(8)
        else:
            data[j] -= 1


# print(0, len(data))
for i in range(0, 256):
    # run(256 - i)
    offsets[i % 7] += carry1[i % 7]
    carry1[i % 7] = carry2[i % 7]
    carry2[i % 7] = 0
    carry2[(i+2) % 7] = offsets[i % 7]

    print(i, sum(offsets.values()) + sum(carry1) +
          sum(carry2)) #, len(data), offsets, carry1, carry2)
