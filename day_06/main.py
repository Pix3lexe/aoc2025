import math


def part_1(path):
    problems = []
    with open(path, "r") as f:
        for line in f:
            parts = line.split()
            if not problems:
                problems = [[item] for item in parts if item.strip()]
            else:
                for i, part in enumerate(parts):
                    problems[i].append(part.strip())

    ans = 0
    for problem in problems:
        op = problem[-1]
        tmp = int(problem[0])
        for num_str in problem[1 : len(problem) - 1]:
            num = int(num_str)
            if op == "+":
                tmp += num
            else:
                tmp *= num

        ans += tmp
    return ans


def part_2(path):
    grid = []
    with open(path, "r") as f:
        grid = f.readlines()

    ans = 0

    cur_nums = []
    for j in range(len(grid[0]) - 1, -1, -1):
        num = ""
        for i in range(len(grid)):
            letter = grid[i][j]
            if not letter.strip():
                continue
            if letter in "+*":
                if num.strip():
                    cur_nums.append(num)

                if letter == "+":
                    ans += sum([int(num_str) for num_str in cur_nums])
                else:
                    ans += math.prod([int(num_str) for num_str in cur_nums])
                cur_nums.clear()
                num = ""

            else:
                num += letter
        if num.strip():
            cur_nums.append(num)

    return ans


if __name__ == "__main__":
    ans = part_1("in/cur.in")
    print(ans)
    ans2 = part_2("in/cur.in")
    print(ans2)
