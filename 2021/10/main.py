from typing import List


OPENING = "([{<"
CLOSING = ")]}>"


assert len(OPENING) == len(CLOSING)


SCORES_FIRST = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

SCORES_SECOND = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def check_line(line: str) -> str:
    stack: List[str] = []
    for c in line:
        # print(stack)
        if c in OPENING:
            stack.append(c)
        elif c in CLOSING:
            for b in range(len(OPENING)):
                if c == CLOSING[b] and stack[-1] != OPENING[b]:
                    return c
                elif c == CLOSING[b] and stack[-1] == OPENING[b]:
                    # print("d", stack)
                    stack.pop()
        else:
            raise ValueError(f"Unexpected character: {c}")
    return ""


def complete_line(line: str) -> str:
    stack: List[str] = []
    for c in line:
        # print(stack)
        if c in OPENING:
            stack.append(c)
        elif c in CLOSING:
            for b in range(len(OPENING)):
                if c == CLOSING[b] and stack[-1] != OPENING[b]:
                    return c
                elif c == CLOSING[b] and stack[-1] == OPENING[b]:
                    # print("d", stack)
                    stack.pop()
        else:
            raise ValueError(f"Unexpected character: {c}")
    out = ""
    for r in reversed(stack):
        out += CLOSING[OPENING.find(r)]
    return out


test = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def main(f: List[str]) -> None:
    # first_part = 0
    # for e, line in enumerate(f):
    #     ch = check_line(line[:-1])
    #     # print(f"{e}: {ch}")
    #     if ch != "":
    #         first_part += SCORES_FIRST[ch]

    # print(first_part)

    filtered = list(filter((lambda x: check_line(x) == ""), f))
    out = []
    for i in filtered:
        line_score = 0
        temp = complete_line(i)
        for j in temp:
            line_score *= 5
            line_score += SCORES_SECOND[j]
        out.append(line_score)
    print(sorted(out)[len(out) // 2])


with open("data.txt") as f:
    inp = list(map((lambda x: x[:-1]), f))
    main(inp)

# main(test)