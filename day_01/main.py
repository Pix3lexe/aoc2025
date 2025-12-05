def part_1(path):
    instructions: list[str] = []
    with open(path, "r") as f:
        instructions = f.readlines()

    cur = 50
    end = 100
    cnt = 0
    for move in instructions:
        if cur == 0:
            cnt += 1
        dir = move[0]
        deg = int(move[1:])
        sign = 1 if dir == "R" else -1
        cur = (cur + sign * deg) % end

    return cnt


def part_2(path):
    instructions: list[str] = []
    with open(path, "r") as f:
        instructions = f.readlines()

    cur = 50
    end = 100
    cnt = 0
    for move in instructions:
        dir = move[0]
        deg = int(move[1:])
        sign = 1 if dir == "R" else -1
        for _ in range(deg):
            cur += sign
            cur %= end
            cnt += cur == 0

    return cnt


if __name__ == "__main__":
    ans = part_1("in/cur.in")
    ans2 = part_2("in/cur.in")
    print(ans)
    print(ans2)
