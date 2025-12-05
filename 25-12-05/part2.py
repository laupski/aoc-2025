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

    ranges = []
    sum = 0

    for range in fresh:
        start, end = range.split("-")
        start = int(start)
        end = int(end)
        ranges.append((start, end))

    ranges.sort()  # this works but it should be with a lambda function

    # print(ranges)
    merged = [ranges[0]]
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:  # Overlapping or adjacent
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    # print(merged)
    for range in merged:
        sum += range[1] - range[0] + 1

    return sum


def main():
    sum = solve_cafeteria_puzzle("25-12-05/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
