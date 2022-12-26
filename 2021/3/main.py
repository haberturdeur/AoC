counted = [int(0) for i in range(12)]
file = []
counter = 0
with open("data.txt", "rt") as data:
    for line in data:
        counter += 1
        file.append([])
        for e, i in enumerate(line[:-1]):
            counted[e] += int(i)
            file[-1].append(int(i))
    gamma = ""
    epsilon = ""
    for i in counted:
        if i > counter / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    oxygenA = file[:]
    coA = file[:]

    # for e, i in enumerate(counted):
    #     tempO = 0
    #     if (counter % 2 == 0 and i == counter // 2) or i > counter // 2:
    #         tempO = 1
    #     # oxygenA = [a for a in oxygenA if a[e] == tempO]
    #     oxygenA = list(filter((lambda x: x[e] == tempO), oxygenA))
    #     print(len(oxygenA))
    #     if len(oxygenA) == 1:
    #         break

    # for e, i in enumerate(counted):
    #     tempCO = 1
    #     if (counter % 2 == 0 and i == counter // 2) or i < counter // 2:
    #         tempCO = 0
    #     coA = list(filter((lambda x: x[e] == tempCO), coA))
    #     # coA = [a for a in coA if a[e] == tempCO]
    #     print(len(coA))
    #     if len(coA) == 1:
    #         break

    for i in range(12):
        count = 0
        for j in oxygenA:
            count += j[i]
        tempO = 0
        if count >= len(oxygenA) / 2:
            tempO = 1
        oxygenA = list(filter((lambda x: x[i] == tempO), oxygenA))
        print(len(oxygenA))
        if len(oxygenA) == 1:
            break

    for i in range(12):
        count = 0
        for j in coA:
            count += j[i]
        tempCO = 0
        if count < len(coA) / 2:
            tempCO = 1
        coA = list(filter((lambda x: x[i] == tempCO), coA))
        if len(coA) == 1:
            break

    print(len(oxygenA))
    print(len(coA))

    co = ""
    o = ""

    for i in range(12):
        co += str(coA[0][i])
        o += str(oxygenA[0][i])
  
    print(int(gamma, 2))
    print(int(epsilon, 2))
    print(int(epsilon, 2)*int(gamma, 2))
    print("")
    print(int(o, 2))
    print(int(co, 2))
    print(int(o, 2)*int(co, 2))