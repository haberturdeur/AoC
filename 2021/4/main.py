import re


def check_win(card):
    for line in card:
        out = 0
        for number in line:
            out += number
        if out == -5:
            return True
    for x in range(5):
        out = 0
        for y in range(5):
            out += card[y][x]
        if out == -5:
            return True
    return False


def calculate_score(card):
    out = 0
    for line in card:
        for number in line:
            if number >= 0:
                out += number
    out *= i
    return out


def check_card(card, number):
    for line in card:
        for e, number in enumerate(line):
            if number == i:
                line[e] = -1
    return check_win(card)


with open("data.txt", "rt") as file:
    line = file.readline()
    numbers = []
    for i in line.split(","):
        numbers.append(int(i))

    cards = []

    line = file.readline()
    while line != "":
        if line == "\n":
            cards.append([])
            for i in range(5):
                line = file.readline()
                cards[-1].append([])
                for j in re.findall(r"\d+", line[:-1]):
                    cards[-1][-1].append(int(j))
        line = file.readline()

    for i in numbers:
        removed_cards = 0
        for e, card in enumerate(cards[:]):
            if check_card(card, i):
                if len(cards) == 1:
                    print(calculate_score(card))
                    exit()
                del cards[e - removed_cards]
                removed_cards += 1