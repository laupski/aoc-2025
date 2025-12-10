try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_rectangles(file_path: str) -> int:
    with open(file_path) as f:
        coordinates = []
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                coordinates.append((x, y))

    max_area = 0
    n = len(coordinates)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            max_area = max(max_area, area)

    return max_area


def main():
    answer = solve_rectangles("25-12-09/input.txt")
    print(answer)


if __name__ == "__main__":
    main()
