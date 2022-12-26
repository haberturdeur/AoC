from typing import Dict, List, Set
from copy import copy


class Accumulator:
    def __init__(self) -> None:
        self.visited: List[str] = []
        self.double = False

    def __copy__(self) -> "Accumulator":
        out = Accumulator()
        out.double = copy(self.double)
        out.visited = self.visited[:]
        return out


class Node:
    def __init__(self, name: str):
        self.name = name
        self.children: Set["Node"] = set()

    def is_big(self) -> bool:
        return self.name.isupper()

    def can_visit(self, acc: Accumulator) -> bool:
        if self.is_big() or self.name not in acc.visited:
            return True
        if acc.double or self.name in ["start", "end"]:
            return False
        acc.double = True
        return True

    def get_paths(self,
                  acc: Accumulator) -> List[List[str]]:
        acc.visited.append(self.name)
        if self.name == "end":
            return [acc.visited]
        out: List[List[str]] = []
        for node in self.children:
            temp = copy(acc)
            if node.can_visit(temp):
                out.extend(node.get_paths(temp))
        return out


def parse(data: List[str]) -> Dict[str, Node]:
    nodes = {"start": Node("start"), "end": Node("end")}

    for line in data:
        temp = line.split("-")
        nodes.setdefault(temp[0], Node(temp[0]))
        nodes.setdefault(temp[1], Node(temp[1]))
        nodes[temp[0]].children.add(nodes[temp[1]])
        nodes[temp[1]].children.add(nodes[temp[0]])
    return nodes


def read_file() -> Dict[str, Node]:

    temp = []
    with open("data.txt") as f:
        for line in f:
            temp.append(line[:-1])
    return parse(temp)


test = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc"
]

nodes = read_file()
# nodes = parse(test)

paths = nodes["start"].get_paths(Accumulator())
print(len(paths))

for path in paths:
    for node in path:
        print(node, end=",")
    print("")


print(len(paths))
