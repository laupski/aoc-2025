try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_junctions_puzzle(filename) -> int:
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f.readlines()]

    # Parse junctions
    junctions = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        junctions.append((x, y, z))

    n = len(junctions)

    # Union-Find data structures
    parent = list(range(n))
    rank = [0] * n
    num_circuits = n  # Track number of separate circuits

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        nonlocal num_circuits
        px, py = find(x), find(y)
        if px == py:
            return False  # Already in same circuit
        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        num_circuits -= 1
        return True

    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = junctions[i]
            x2, y2, z2 = junctions[j]
            # Using squared distance to avoid sqrt (order is preserved)
            dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
            distances.append((dist_sq, i, j))

    # Sort by distance
    distances.sort()

    # Connect pairs until all in one circuit
    last_i, last_j = None, None
    for dist_sq, i, j in distances:
        if num_circuits == 1:
            break
        if union(i, j):
            last_i, last_j = i, j  # Track last successful connection

    # Return product of X coordinates of last two connected boxes
    result = junctions[last_i][0] * junctions[last_j][0]

    return result


def main():
    # Test with sample - should get 216 * 117 = 25272
    # answer = solve_junctions_puzzle("25-12-08/sample.txt")
    # print(f"Sample answer: {answer}")

    answer = solve_junctions_puzzle("25-12-08/input.txt")
    print(f"Input answer: {answer}")


if __name__ == "__main__":
    main()
