from dijkstar import Graph, find_path

data = []

with open("data.txt") as f:
    for line in f:
        data.append([])
        for c in line[:-1]:
            data[-1].append(int(c))


def cut_values(value):
    c = value % 10 + value // 10
    return cut_values(c) if c > 9 else c


def get_value(x, y, cost):
    c = (cost[y % len(cost)][x % len(cost[0])] +
         y // len(cost) + x // len(cost[0]))
    return cut_values(c)


def price(x, y):
    # global data
    # o_x, o_y = u % len(data[0]), u // len(data[0])
    # d_x, d_y = v % len(data[0]), v // len(data[0])

    # direction = (d_x - o_x, d_y - o_y)

    # if direction == (1, 0):
    #     return get_value(d_x, d_y, data)
    # if direction == (0, 1):
    #     return get_value(d_x, d_y, data)

    # if direction == (-1, 0):
    #     return get_value(o_x, o_y, data)
    # if direction == (0, -1):
    #     return get_value(o_x, o_y, data)
    global data
    return get_value(x, y, data)

def get_graph(width, height):
    graph = Graph()
    for y in range(height):
        for x in range(width):
            curr = y*width + x
            if x < width-1:
                graph.add_edge(curr, curr + 1, price(x+1, y))
            if y < height-1:
                graph.add_edge(curr, curr + width, price(x, y+1))
            if x > 0:
                graph.add_edge(curr, curr - 1, price(x-1, y))
            if y > 0:
                graph.add_edge(curr, curr - width, price(x, y-1))
    return graph


def min_cost(cost, n, m):
    tc = [[0 for _ in range(m+1)]for _ in range(n+1)]
    tc[0][0] = cost[0][0]
    # print(n, m)

    # for y in range(m+1):
    #     for x in range(n+1):
    #         c = (cost[y % len(cost)][x % len(cost[0])] +
    #              y // len(cost) + x // len(cost[0]))
    #         print(c % 10 + min(c // 10, 1), end="")
    #     print("")

    for y in range(1, m+1):
        c = (cost[y % len(cost)][0] + y // len(cost))
        tc[y][0] = tc[y-1][0] + cut_values(c)

    for x in range(1, n+1):
        c = (cost[0][x % len(cost[0])] + x // len(cost[0]))
        tc[0][x] = tc[0][x-1] + cut_values(c)

    for y in range(1, m+1):
        for x in range(1, n+1):
            c = (cost[y % len(cost)][x % len(cost[0])] +
                 y // len(cost) + x // len(cost[0]))
            tc[y][x] = min(tc[y-1][x], tc[y][x-1]) + cut_values(c)

    return tc[m][n]


# print(min_cost(data, 498, 498) - data[0][0])
# print(get_graph(10, 10))
print(find_path(get_graph(100, 100), 0, 9999))
print(find_path(get_graph(500, 500), 0, 499*500+499))