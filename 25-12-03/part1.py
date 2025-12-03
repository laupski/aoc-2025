try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_battery_puzzle(filename):
    with open(filename, "r") as f:
        batteries = f.read().strip().split("\n")

    sum = 0

    for joltages in batteries:
        start = 0
        maxVoltage = 0
        for remaining in range(2, 0, -1):
            end = len(joltages) - (remaining - 1)
            best_idx = find_biggest_digit(joltages, start, end)
            maxVoltage += int(joltages[best_idx]) * pow(10, remaining - 1)
            start = best_idx + 1
        sum += maxVoltage

    return sum


@profile
def find_biggest_digit(s, start, end):
    max_digit = -1
    max_index = -1
    for i in range(start, end):
        digit = int(s[i])
        if digit > max_digit:
            max_digit = digit
            max_index = i
    return max_index


def main():
    sum = solve_battery_puzzle("25-12-03/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
