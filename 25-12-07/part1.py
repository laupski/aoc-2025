try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_beams_puzzle(filename) -> int:
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    height = len(lines)
    width = len(lines[0]) if lines else 0

    start_col = None
    for col, char in enumerate(lines[0]):
        if char == "S":
            start_col = col
            break

    if start_col is None:
        return 0

    splitters = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == "^":
                splitters.add((row, col))

    split_count = 0

    active_beams = {start_col}

    for row in range(1, height):
        new_beams = set()

        for col in active_beams:
            if (row, col) in splitters:
                split_count += 1
                if col - 1 >= 0:
                    new_beams.add(col - 1)
                if col + 1 < width:
                    new_beams.add(col + 1)
            else:
                new_beams.add(col)

        active_beams = new_beams

        if not active_beams:
            break

    return split_count


def main():
    splits = solve_beams_puzzle("25-12-07/input.txt")
    print(splits)


if __name__ == "__main__":
    main()
