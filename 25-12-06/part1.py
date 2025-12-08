try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_cephalopod_puzzle(filename) -> int:
    with open(filename, "r") as f:
        lines = f.readlines()

    number_rows = [line.split() for line in lines[:-1]]
    operators = lines[-1].split()

    column_results = []
    for col_idx, op in enumerate(operators):
        col_numbers = [int(row[col_idx]) for row in number_rows]

        if op == "*":
            result = 1
            for num in col_numbers:
                result *= num
        else:
            result = sum(col_numbers)

        column_results.append(result)

    return sum(column_results)


def main():
    sum = solve_cephalopod_puzzle("25-12-06/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
