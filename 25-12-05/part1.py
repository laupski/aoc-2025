try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_cafeteria_puzzle(filename) -> int:
    with open(filename, "r") as f:
        content = f.read()

    sections = content.strip().split("\n\n")
    fresh = sections[0].split("\n")
    database = sections[1].split("\n") if len(sections) > 1 else []

    lookup = set()
    sum = 0

    for orange in database:
        for ranges in fresh:
            start, end = ranges.split("-")
            start = int(start)
            end = int(end)
            if (int(orange) not in lookup) and (start <= int(orange) <= end):
                lookup.add(int(orange))
                sum += 1

    return sum


def main():
    sum = solve_cafeteria_puzzle("25-12-05/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
