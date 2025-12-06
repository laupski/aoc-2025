try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_cephalopod_puzzle(filename) -> int:
    with open(filename, "r") as f:
        lines = f.readlines()

    all_lines = [line.rstrip("\n") for line in lines]
    max_len = max(len(line) for line in all_lines)

    # Find dividers
    dividers = []
    for pos in range(max_len):
        is_divider = True
        for line in all_lines:
            if line[pos] != " ":
                is_divider = False
                break
        if is_divider:
            dividers.append(pos)

    # Create column ranges from dividers
    column_ranges = []
    start = 0
    for div in dividers:
        if div > start:
            column_ranges.append((start, div - 1))
        start = div + 1
    if start < max_len:
        column_ranges.append((start, max_len - 1))

    number_lines = all_lines[:-1]
    operator_line = all_lines[-1]
    # print(dividers)
    # print(number_lines)
    # print(operator_line)
    # print(column_ranges)

    results = []
    for start, end in column_ranges:
        # print(start,end)
        numbers = []
        for i in range(end, start - 1, -1):
            num = ""
            # print(i)
            for digit in range(0, 4):
                # print(number_lines[digit][i])
                if number_lines[digit][i] != " ":
                    num = num + number_lines[digit][i]
            # print(num)
            if num != "":
                numbers.append(int(num))

        # print(numbers)
        op = operator_line[start : end + 1].strip()[0]

        result = 1 if op == "*" else 0
        for n in numbers:
            result = result * n if op == "*" else result + n

        results.append(result)

    return sum(results)


def main():
    sum = solve_cephalopod_puzzle("25-12-06/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
