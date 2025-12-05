import numpy as np


def part_1(path):
    banks = []
    with open(path, "r") as f:
        for line in f.readlines():
            banks.append([int(bat) for bat in line if bat != "\n"])

    summ = 0
    for bank in banks:

        max_ind1 = np.argmax(bank[: len(bank) - 1])
        max_ind2 = np.argmax(bank[max_ind1 + 1 :]) + max_ind1 + 1
        summ += int(bank[max_ind1] * 10 + bank[max_ind2])

    return summ


def part_2(path):
    banks = []
    with open(path, "r") as f:
        for line in f.readlines():
            banks.append([int(bat) for bat in line if bat != "\n"])

    summ = 0
    for bank in banks:
        num = ""
        prev_max = -1
        for offset in range(1, 13):
            index = (
                np.argmax(bank[prev_max + 1 : len(bank) - (12 - offset)]) + prev_max + 1
            )
            prev_max = index
            num += str(bank[index])

        summ += int(num)

    return summ


if __name__ == "__main__":
    ans = part_1("in/cur.in")
    ans2 = part_2("in/cur.in")
    print(ans)
    print(ans2)
