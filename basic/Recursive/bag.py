"""
w
v

"""





def func1(w, v, weights):

    def process(w, v, idx, rest_weights, n):
        if rest_weights < 0:
            return -1

        if idx == n:
            return 0

        # two case
        value = -1
        case_1 = process(w, v, idx+1, rest_weights-w[idx], n)
        case_2 = process(w, v, idx+1, rest_weights, n)
        if case_1 != -1:
            value = case_1 + v[idx]

        return max(value, case_2)

    return process(w, v, 0, weights, len(w))


def func2(w, v, weights):

    def process(w, v, idx, rest_weights, n):
        cache = [[-1 for i in range(rest_weights+1)] for j in range(n+1)]
        for i in range(rest_weights+1):
            cache[n][i] = 0

        for i in range(n-1, -1, -1):
            for j in range(rest_weights+1):
                cache[i][j] = cache[i+1][j]
                if rest_weights >= w[i]:
                    cache[i][j] = max(cache[i][j], v[i]+cache[i+1][j-w[i]])
