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
        nums = []
        for offset in range(12):
            index = np.argmax(bank[11 - offset : len(bank) - offset]) + offset
            nums.append(bank[index])

        num_str = "".join(nums)
        summ += int(num_str)

    return summ


if __name__ == "__main__":
    ans = part_1("in.txt")
    ans2 = part_2("in.txt")
    print(ans)
    print(ans2)
