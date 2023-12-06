d1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def parse(data: str) -> list:
    lines = data.split("\n")

    out: list[dict[int: int]] = []
    # normalize data
    for line in range(len(lines)):
        newline: list[str, str] = lines[line][lines[line].index(":") + 2:].replace("  ", " ").replace(" | ", "|").split("|")
        newline[0] = sorted(list(map(int, filter(None, newline[0].split(" ")))))     # im sorry
        newline[1] = sorted(list(map(int, filter(None, newline[1].split(" ")))))
        out.append(dict(zip(newline[0], newline[1])))

    return out


def determine_matches_and_output_score(data: list[dict[int: int]]):
    pass


parse(d1)