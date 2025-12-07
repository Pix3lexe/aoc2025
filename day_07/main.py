from collections import deque
from functools import lru_cache


def part_1(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([c for c in line])

    ROWS, COLS = len(grid), len(grid[0])
    start = (0, 0)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "S":
                start = (i, j)

    def in_bounds(i, j):
        return 0 <= i < ROWS and 0 <= j < COLS

    queue = deque([start])

    split = 0
    while queue:
        while queue:
            i, j = queue.popleft()
            if grid[i][j] == "|":
                continue
            grid[i][j] = "|"
            next_i, next_j = i + 1, j
            if not in_bounds(next_i, next_j):
                continue

            if grid[next_i][next_j] == "|":
                continue

            if grid[next_i][next_j] == "^":
                split += 1
                left = (next_i, j - 1)
                right = (next_i, j + 1)

                if in_bounds(*left) and grid[left[0]][left[1]] == ".":
                    queue.append(left)

                if in_bounds(*right) and grid[right[0]][right[1]] == ".":
                    queue.append(right)

            else:
                queue.append((next_i, next_j))

    return split


def part_2(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([c for c in line])

    ROWS, COLS = len(grid), len(grid[0])
    start = (0, 0)
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "S":
                start = (i, j)

    def in_bounds(i, j):
        return 0 <= i < ROWS and 0 <= j < COLS

    @lru_cache(None)
    def count_paths(i, j):
        ni, nj = i + 1, j

        if not in_bounds(ni, nj):
            return 1

        cell = grid[ni][nj]

        if cell == "^":
            total = 0

            if in_bounds(ni, nj - 1):
                total += count_paths(ni, nj - 1)

            if in_bounds(ni, nj + 1):
                total += count_paths(ni, nj + 1)

            return total

        return count_paths(ni, nj)

    return count_paths(*start)


if __name__ == "__main__":
    print(part_1("in/cur.in"))
    print(part_2("in/cur.in"))
