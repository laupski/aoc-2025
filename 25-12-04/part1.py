try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_toilet_paper_puzzle(filename):
    with open(filename, "r") as f:
        matrix = [list(line.strip()) for line in f]

    sum = 0
    width = len(matrix[0])
    height = len(matrix)
    for row in range(height):
        for col in range(width):
            char = matrix[row][col]
            neighbors = get_neighbors(matrix, row, col)
            if neighbors < 4 and char == "@":
                sum += 1
    return sum


@profile
def get_neighbors(matrix, row: int, col: int) -> int:
    neighbors = 0
    # nlist = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == "@":
                neighbors += 1
                # nlist.append(matrix[r][c])

    # print(nlist)
    return neighbors


def main():
    sum = solve_toilet_paper_puzzle("25-12-04/input.txt")
    print(sum)


if __name__ == "__main__":
    main()
