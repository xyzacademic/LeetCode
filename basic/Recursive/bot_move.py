"""
An array length of N, robot at position M, K steps moves to p
"""

def func1(n, m, k, p):
    if n < 1 or abs(p-m) > k:
        return 0

    def process(n, current_position, rest_steps, p):
        if rest_steps == 0:
            return 1 if current_position == p else 0

        if current_position == 0:
            return process(n, current_position + 1, rest_steps - 1, p)

        if current_position == n - 1:
            return process(n, current_position - 1, rest_steps - 1, p)

        return process(n, current_position - 1, rest_steps - 1, p) + \
               process(n, current_position + 1, rest_steps - 1, p)

    return process(n, m, k, p)


def func2(n, m, k, p):
    if n < 1 or abs(p-m) > k:
        return 0

    cache = [[None for i in range(n)] for i in range (k+1)]

    def process(n, current_position, rest_step, p, cache):

        if cache[rest_step][current_position]!= None:
            return cache[rest_step][current_position]

        if rest_step == 0:
            if current_position == p:
                cache[rest_step][current_position] = 1
            else:
                cache[rest_step][current_position] = 0
            return cache[rest_step][current_position]

        if current_position == 0:
            cache[rest_step][current_position] = process(n, current_position+1, rest_step-1, p, cache)
            return cache[rest_step][current_position]

        if current_position == n-1:
            cache[rest_step][current_position] = process(n, current_position-1, rest_step-1, p, cache)
            return cache[rest_step][current_position]

        cache[rest_step][current_position] = process(n, current_position-1, rest_step-1, p, cache) + \
                                             process(n, current_position+1, rest_step-1, p, cache)

        return cache[rest_step][current_position]

    return process(n, m, k, p, cache)



def func3(n, m, k, p):
    if n < 1 or abs(m-p) > k:
        return 0


    def process(n, m, k, p):
        cache = [[None for i in range(n)] for j in range(k+1)]
        for i in range(n):
            if i != p:
                cache[0][i] = 0
        cache[0][p] = 1
        for step in range(1, k+1):
            for current_position in range(n):
                if current_position == 0:
                    cache[step][current_position] = cache[step-1][current_position+1]
                elif current_position == n-1:
                    cache[step][current_position] = cache[step-1][current_position-1]
                else:
                    cache[step][current_position] = cache[step-1][current_position+1] + cache[step-1][current_position-1]
        # print(cache)
        return cache[k][m]

    return process(n, m, k, p)



if __name__ == '__main__':
    n = 7
    m = 3
    k = 6
    p = 5
    from time import time
    a = time()
    for i in range(100):
        func1(n, m, k, p)
    print('cost: ', time()-a)

    a = time()
    for i in range(100):
        func2(n, m, k, p)
    print('cost: ', time()-a)
    a = time()
    for i in range(100):
        func3(n, m, k, p)
    print('cost: ', time()-a)
