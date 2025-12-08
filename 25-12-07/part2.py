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

    timeline_counts = {start_col: 1}

    for row in range(1, height):
        new_counts = {}

        for col, count in timeline_counts.items():
            if (row, col) in splitters:
                if col - 1 >= 0:
                    new_counts[col - 1] = new_counts.get(col - 1, 0) + count
                if col + 1 < width:
                    new_counts[col + 1] = new_counts.get(col + 1, 0) + count
            else:
                new_counts[col] = new_counts.get(col, 0) + count

        timeline_counts = new_counts

        if not timeline_counts:
            break

    return sum(timeline_counts.values())


def main():
    result = solve_beams_puzzle("25-12-07/input.txt")
    print(result)


if __name__ == "__main__":
    main()
