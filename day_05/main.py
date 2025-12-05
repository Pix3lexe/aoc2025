def part_1(path):
    with open(path, "r") as f:
        content = f.read()
        sections = content.split("\n\n")
        freshs = sections[0].splitlines()
        ids = set([int(num) for num in sections[1].splitlines()])

    fresh = set()

    for id in ids:
        for s in freshs:
            n1, n2 = s.split("-")
            if int(n1) <= id <= int(n2):
                fresh.add(id)

    ans = len(fresh)
    return ans


def part_2(path):
    with open(path, "r") as f:
        content = f.read()
        sections = content.split("\n\n")
        freshs = sections[0].splitlines()

    intervals = []

    for s in freshs:
        n1, n2 = map(int, s.split("-"))
        intervals.append((n1, n2))

    intervals.sort()
    merged = []
    cur_start, cur_end = intervals[0]
    for s, e in intervals[1:]:
        if s <= cur_end + 1:
            cur_end = max(cur_end, e)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e

    merged.append((cur_start, cur_end))

    ans = sum(b - a + 1 for a, b in merged)
    return ans


if __name__ == "__main__":
    ans = part_1("in/cur.in")
    print(ans)
    ans2 = part_2("in/cur.in")
    print(ans2)
