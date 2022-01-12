"""

"""


def find_one_order(arr):
    eor = 0
    for num in arr:
        eor ^= num

    return eor


def find_two_order(arr):

    eor = 0
    for num in arr:
        eor ^= num

    right_one = eor & (~eor + 1)

    a = []
    eor_ = 0
    for num in arr:
        if num & right_one != 0:
            eor_ ^= num

    return eor_, eor_ ^ eor









if __name__ == '__main__':
    a = [3, 3, 4, 4, 5, 5, 1, 2, 2, 7, 7]
    b = [3, 3, 4, 4, 5, 5, 1, 2, 2, 7, 7, 7]

    print(find_one_order(a))
    print(find_two_order(b))