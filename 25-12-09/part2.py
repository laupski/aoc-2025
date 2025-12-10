try:
    profile
except NameError:

    def profile(func):
        return func


@profile
def point_in_polygon(x: int, y: int, polygon: list[tuple[int, int]]) -> bool:
    n = len(polygon)
    inside = False

    # Check if point is on an edge
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Check if point is on a horizontal segment
        if y1 == y2 == y and min(x1, x2) <= x <= max(x1, x2):
            return True
        # Check if point is on a vertical segment
        if x1 == x2 == x and min(y1, y2) <= y <= max(y1, y2):
            return True

    # Ray casting algorithm
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i

    return inside


@profile
def segments_intersect_interior(
    ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int
) -> bool:
    # Segment A is horizontal, B is vertical
    if ay1 == ay2 and bx1 == bx2:
        # A: horizontal at y=ay1, from x=min(ax1,ax2) to x=max(ax1,ax2)
        # B: vertical at x=bx1, from y=min(by1,by2) to y=max(by1,by2)
        a_min_x, a_max_x = min(ax1, ax2), max(ax1, ax2)
        b_min_y, b_max_y = min(by1, by2), max(by1, by2)
        # Interior intersection: strict inequalities
        if a_min_x < bx1 < a_max_x and b_min_y < ay1 < b_max_y:
            return True

    # Segment A is vertical, B is horizontal
    if ax1 == ax2 and by1 == by2:
        # A: vertical at x=ax1, from y=min(ay1,ay2) to y=max(ay1,ay2)
        # B: horizontal at y=by1, from x=min(bx1,bx2) to x=max(bx1,bx2)
        a_min_y, a_max_y = min(ay1, ay2), max(ay1, ay2)
        b_min_x, b_max_x = min(bx1, bx2), max(bx1, bx2)
        # Interior intersection: strict inequalities
        if b_min_x < ax1 < b_max_x and a_min_y < by1 < a_max_y:
            return True

    return False


@profile
def rectangle_inside_polygon(
    x1: int, y1: int, x2: int, y2: int, polygon: list[tuple[int, int]]
) -> bool:
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    corners = [
        (min_x, min_y),
        (min_x, max_y),
        (max_x, min_y),
        (max_x, max_y),
    ]

    for cx, cy in corners:
        if not point_in_polygon(cx, cy, polygon):
            return False

    # Define rectangle edges
    rect_edges = [
        # Bottom edge (horizontal)
        (min_x, min_y, max_x, min_y),
        # Top edge (horizontal)
        (min_x, max_y, max_x, max_y),
        # Left edge (vertical)
        (min_x, min_y, min_x, max_y),
        # Right edge (vertical)
        (max_x, min_y, max_x, max_y),
    ]

    n = len(polygon)
    for i in range(n):
        px1, py1 = polygon[i]
        px2, py2 = polygon[(i + 1) % n]

        for rx1, ry1, rx2, ry2 in rect_edges:
            if segments_intersect_interior(rx1, ry1, rx2, ry2, px1, py1, px2, py2):
                return False

    return True


@profile
def solve_rectangles(file_path: str) -> int:
    with open(file_path) as f:
        coordinates = []
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(","))
                coordinates.append((x, y))

    polygon = coordinates

    max_area = 0
    n = len(coordinates)

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]

            if rectangle_inside_polygon(x1, y1, x2, y2, polygon):
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                max_area = max(max_area, area)

    return max_area


def main():
    answer = solve_rectangles("25-12-09/input.txt")
    print(answer)


if __name__ == "__main__":
    main()
