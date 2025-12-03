try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_id_puzzle(filename):
    with open(filename, "r") as f:
        ids = f.read().strip()

    sum = 0

    for id in ids.split(","):
        start, end = id.split("-")
        start = int(start)
        end = int(end)
        for i in range(start, end):
            if isRepeat(i):
                sum += i

    return sum


@profile
def isRepeat(num: int) -> bool:
    snum = str(num)
    length = len(snum)

    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue

        pattern = snum[:pattern_len]
        repetitions = length // pattern_len

        if pattern * repetitions == snum:
            return True

    return False


def main():
    sum = solve_id_puzzle("25-12-02/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
