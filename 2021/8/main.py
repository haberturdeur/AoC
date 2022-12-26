import re
from typing import Dict, List, Set, Tuple

Segment = str
Segments = Segment
Original = Segment
New = Segment
Digit = int
Used = Dict[Digit, Set[Segment]]
Conversion = Dict[Original, Set[New]]

data: List[Tuple[List[Segments],
                 List[Segments]]]= []
                #  Used,
                #  Conversion]] = []

SEGMENTS = [{"a", "b", "c", "e", "f", "g"},
            {"c", "f"},
            {"a", "c", "d", "e", "g"},
            {"a", "c", "d", "f", "g"},
            {"b", "c", "d", "f"},
            {"a", "b", "d", "f", "g"},
            {"a", "b", "d", "e", "f", "g"},
            {"a", "c", "f"},
            {"a", "b", "c", "d", "e", "f", "g"},
            {"a", "b", "c", "d", "f", "g"}]

with open("data.txt") as f:
    for line in f:
        j = re.match(r"(.+?) \| (.+)", line[:-1])
        data.append(([set([c for c in i]) for i in j[1].split(" ")],
                     [set([c for c in i]) for i in j[2].split(" ")]))
                    #  {k: {"a", "b", "c", "d", "e", "f", "g"}
                    #      for k in range(10)},
                    #  {k: {"a", "b", "c", "d", "e", "f", "g"} for k in {"a", "b", "c", "d", "e", "f", "g"}}))

count = 0

# def update(values, used: Used, conversion: Conversion, digit: Digit) -> None:
#     used[digit] = set([c for c in values])
#     for c in SEGMENTS[digit]:
#         conversion[c] = used[digit]
#     for d in SEGMENTS[8].difference(SEGMENTS[digit]):
#         conversion[d].difference_update(used[digit])
#     for i in range(9):
#         if i != digit:
#             if len(used[i].intersection(used[digit])) == 0:
#                 used[i].difference_update(used[digit])



# for inp, values, used, conversion in data:
#     for value in values:
#         if len(value) == 2:  # 1
#             update(value, used, conversion, 1)
#             count += 1
#         elif len(value) == 3:  # 7
#             update(value, used, conversion, 7)
#             count += 1
#         elif len(value) == 4:  # 4
#             update(value, used, conversion, 4)
#             count += 1
#         elif len(value) == 5:  # 2, 3, 5
#             if len(.intersection)
#         elif len(value) == 6:  # 0, 6, 9
#             update(value, used, conversion, 0)
#             update(value, used, conversion, 6)
#             update(value, used, conversion, 9)
            
#         elif len(value) == 7:  # 8
#             count += 1

# for inp, values, used, conversion in data:
#     print(f"{inp}\n\t{values}\n\t{used}\n\t{conversion}")

out = 0

for first, values in data:
    signals = first + values
    one = {}
    four = {}
    for i in signals:
        if len(i) == 2:
            one = i
        elif len(i) == 4:
            four = i
    if one == {} or four == {}:
        raise ValueError
    temp = 0
    for value in values:
        if len(value) == 2:  # 1
            temp = temp * 10 + 1
        elif len(value) == 3:  # 7
            temp = temp * 10 + 7
        elif len(value) == 4:  # 4
            temp = temp * 10 + 4
        elif len(value) == 5:  # 2, 3, 5
            if len(value.intersection(one)) == 2:
                temp = temp * 10 + 3
            elif len(value.intersection(four)) == 2:
                temp = temp * 10 + 2
            elif len(value.intersection(four)) == 3:
                temp = temp * 10 + 5
            else:
                raise ValueError
        elif len(value) == 6:  # 0, 6, 9
            if len(value.intersection(four)) == 4:
                temp = temp * 10 + 9
            elif len(value.intersection(one)) == 2:
                temp = temp * 10 + 0
            elif len(value.intersection(one)) == 1:
                temp = temp * 10 + 6
            else:
                raise ValueError
        elif len(value) == 7:
            temp = temp * 10 + 8
        else:
            raise ValueError
    out += temp

print(out)