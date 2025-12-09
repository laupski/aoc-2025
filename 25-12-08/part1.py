try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def solve_junctions_puzzle(filename, num_connections=1000) -> int:
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
    size = [1] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # Already in same circuit
        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        size[px] += size[py]
        if rank[px] == rank[py]:
            rank[px] += 1
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

    # Connect the specified number of closest pairs
    connections_made = 0
    for dist_sq, i, j in distances:
        if connections_made >= num_connections:
            break
        union(i, j)
        connections_made += 1

    # Get circuit sizes - need to find actual roots after all unions
    circuit_sizes = {}
    for i in range(n):
        root = find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    sizes = sorted(circuit_sizes.values(), reverse=True)
    result = sizes[0] * sizes[1] * sizes[2] if len(sizes) >= 3 else 0

    return result


def main():
    # Test with sample - after 10 connections, should get 5*4*2 = 40
    # answer = solve_junctions_puzzle("25-12-08/sample.txt", num_connections=10)
    # print(f"Sample answer: {answer}")

    answer = solve_junctions_puzzle("25-12-08/input.txt", num_connections=1000)
    print(f"Input answer: {answer}")


if __name__ == "__main__":
    main()
