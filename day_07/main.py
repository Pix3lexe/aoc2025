from collections import deque


def in_bounds(coord, grid):
    return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])


def show(grid):
    for row in grid:
        for c in row:
            print(c, end="")
        print()


def part_1(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([c for c in line])

    start = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)

    queue = deque([start])

    split = 0
    while queue:
        while queue:
            i, j = queue.popleft()
            if grid[i][j] == "|":
                continue
            grid[i][j] = "|"
            next_i, next_j = i + 1, j
            if not in_bounds((next_i, next_j), grid):
                continue

            if grid[next_i][next_j] == "|":
                continue

            if grid[next_i][next_j] == "^":
                split += 1
                left = (next_i, j - 1)
                right = (next_i, j + 1)

                if in_bounds(left, grid) and grid[left[0]][left[1]] == ".":
                    queue.append(left)

                if in_bounds(right, grid) and grid[right[0]][right[1]] == ".":
                    queue.append(right)

            else:
                queue.append((next_i, next_j))

    return split


def part_2(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([c for c in line])

    start = (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                start = (i, j)

    final_positions = []

    def dfs(start, visited):
        queue = deque([start])
        local_visited = visited.copy()

        while queue:
            i, j = queue.popleft()
            next_i, next_j = i + 1, j
            if not in_bounds((next_i, next_j), grid):
                final_positions.append((next_i, next_j))
                continue

            cell = grid[next_i][next_j]
            if cell == "^":
                left = (next_i, j - 1)
                right = (next_i, j + 1)

                if in_bounds(left, grid) and left not in local_visited:
                    new_local_visited = local_visited.copy()
                    new_local_visited.add(left)
                    dfs(left, new_local_visited)

                if in_bounds(right, grid) and right not in local_visited:
                    new_local_visited = local_visited.copy()
                    new_local_visited.add(right)
                    dfs(right, new_local_visited)
                return

            else:
                queue.append((next_i, next_j))

    dfs(start, set())
    return len(final_positions)


if __name__ == "__main__":
    print(part_1("in/cur.in"))
    print(part_2("in/cur.in"))
