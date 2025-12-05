def in_bounds(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def part_1(path):
    grid = []
    with open(path, "r") as f:
        for line in f.readlines():
            grid.append([c for c in line if c != "\n"])

    counts = {}
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != "@":
                continue
            neighs = [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1),
                (x + 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x - 1, y - 1),
            ]
            for i, j in neighs:
                if in_bounds(i, j, grid):
                    if (x, y) not in counts:
                        counts[(x, y)] = 0
                    if grid[i][j] == "@":
                        counts[(x, y)] += 1

    ans = 0
    for adj in counts.values():
        if adj < 4:
            ans += 1

    return ans


def part_2(path):
    grid = []
    with open(path, "r") as f:
        for line in f.readlines():
            grid.append([c for c in line if c != "\n"])

    def remove(grid):
        counts = {}
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] != "@":
                    continue
                neighs = [
                    (x + 1, y),
                    (x, y + 1),
                    (x - 1, y),
                    (x, y - 1),
                    (x + 1, y + 1),
                    (x + 1, y - 1),
                    (x - 1, y + 1),
                    (x - 1, y - 1),
                ]
                for i, j in neighs:
                    if in_bounds(i, j, grid):
                        if (x, y) not in counts:
                            counts[(x, y)] = 0
                        if grid[i][j] == "@":
                            counts[(x, y)] += 1

        removed = 0
        for (x, y), adj in counts.items():
            if adj < 4:
                removed += 1
                grid[x][y] = "."
        return grid, removed

    ans = 0
    while True:
        grid, removed = remove(grid)
        ans += removed
        if removed == 0:
            break

    return ans


if __name__ == "__main__":
    ans = part_1("in/cur.in")
    print(ans)
    ans2 = part_2("in/cur.in")
    print(ans2)
