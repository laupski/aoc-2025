def solve_safe_puzzle(filename):
    with open(filename, "r") as f:
        rotations = [line.strip() for line in f if line.strip()]

    position = 50
    zero_count = 0

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        for _ in range(distance):
            if direction == "L":
                position = (position - 1) % 100
            else:
                position = (position + 1) % 100

            if position == 0:
                zero_count += 1

    return zero_count


def main():
    actual_result = solve_safe_puzzle("25-12-01/input.txt")
    print(actual_result)


if __name__ == "__main__":
    main()
