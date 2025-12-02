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


def isRepeat(num: int) -> bool:
    snum = str(num)
    length = len(snum)

    if length < 2 or length % 2 != 0:
        return False

    half = length // 2
    first_half = snum[:half]
    second_half = snum[half:]

    if first_half == second_half:
        return True

    return False


def main():
    sum = solve_id_puzzle("25-12-02/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
