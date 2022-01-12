"""
N queen problem
"""

import math

def func1(n):

    if n in [0, 2, 3]:
        return 0

    records = [None] * n

    def process(x, n, records):

        if x == n:
            return 1

        results = 0
        for y in range(n):
            if is_valid(records, x, y):
                records[x] = y
                results += process(x + 1, n, records)

        return results

    def is_valid(records, x, y):
        if x > 0:
            for x_i in range(x):
                if y == records[x_i] or abs(x_i - x) == abs(records[x_i] - y):
                    return False

        return True

    return process(0, n, records)


def func2(n):
    if n in [0, 2, 3]:
        return 0
    if n > 32:
        return 0

    limit = -1 if n == 32 else (1 << n) - 1

    def process(limit, col_limit, left_limit, right_limit):

        if col_limit == limit:
            return 1

        pos = limit & ~(col_limit | left_limit | right_limit)
        results = 0

        while pos != 0:
            most_right = pos & (~pos + 1)
            pos -= most_right
            results += process(limit, col_limit | most_right, (left_limit | most_right) << 1,
                               (most_right | right_limit) >> 1)

        return results

    return process(limit, 0, 0, 0)




if __name__ == '__main__':
    from time import time
    start = time()
    n = 8

    print(func2(n))
    print(f'cost ', time()-start)

