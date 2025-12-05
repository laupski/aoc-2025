try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_toilet_paper_puzzle(matrix) -> int:
    sum = change_toilet_papers(matrix)
    changes = sum

    while changes != 0:
        changes = change_toilet_papers(matrix)
        sum += changes
    return sum


@profile
def change_toilet_papers(matrix) -> int:
    changes = 0

    width = len(matrix[0])
    height = len(matrix)
    for row in range(height):
        for col in range(width):
            char = matrix[row][col]
            neighbors = get_neighbors(matrix, row, col)
            if neighbors < 4 and char == "@":
                matrix[row][col] = "X"

    for row in range(height):
        for col in range(width):
            if matrix[row][col] == "X":
                changes += 1
                matrix[row][col] = "."

    return changes


@profile
def get_neighbors(matrix, row: int, col: int) -> int:
    neighbors = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = row + dr, col + dc
            if (
                0 <= r < len(matrix)
                and 0 <= c < len(matrix[0])
                and (matrix[r][c] == "@" or matrix[r][c] == "X")
            ):
                neighbors += 1

    return neighbors


def main():
    with open("25-12-04/input.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]
    sum = solve_toilet_paper_puzzle(matrix)
    print(sum)


if __name__ == "__main__":
    main()
