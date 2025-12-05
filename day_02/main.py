import itertools


def part_1(path):
    ids = []
    with open(path, "r") as f:
        ids = f.readline().split(",")

    summ = 0
    for id in ids:
        n1, n2 = id.split("-")
        for num in range(int(n1), int(n2) + 1):
            sub1 = str(num)[: len(str(num)) // 2]
            sub2 = str(num)[len(str(num)) // 2 :]
            if sub1 == sub2:
                summ += num

    return summ


def part_2(path):
    ids = []
    with open(path, "r") as f:
        ids = f.readline().split(",")

    summ = 0
    for id in ids:
        n1, n2 = id.split("-")
        for num in range(int(n1), int(n2) + 1):
            num_str = str(num)
            found = False
            for i in range(1, len(num_str) // 2 + 1):
                if len(num_str) % i != 0:
                    continue
                comp = None
                all_same = True
                for n in itertools.batched(num_str, i):
                    if not comp:
                        comp = n
                    if n != comp:
                        all_same = False
                        break
                if all_same:
                    found = True
                    break
            if found:
                summ += num

    return summ


if __name__ == "__main__":
    ans = part_1("in/cur.in")
    ans2 = part_2("in/cur.in")
    print(ans)
    print(ans2)
