"""
Two person pick card from either side
"""

def func1(arr):

    if len(arr) == 0:
        return 0
    return max(first_order(0, len(arr)-1, arr), second_order(0, len(arr)-1, arr))



def first_order(l, r, arr):
    if l == r:
        return arr[l]

    case_1 = arr[l] + second_order(l+1, r, arr)
    case_2 = arr[r] + second_order(l, r-1, arr)

    return max(case_1, case_2)

def second_order(l, r, arr):
    if l == r:
        return 0

    case_1 = first_order(l+1, r, arr)
    case_2 = first_order(l, r-1, arr)

    return min(case_1, case_2)


def func2(arr):
    n = len(arr)
    dp_f = [[None for i in range(n)] for j in range(n)]
    dp_s = [[None for i in range(n)] for j in range(n)]

    for j in range(n):
        dp_f[j][j] = arr[j]
        dp_s[j][j] = 0
        for i in range(j-1, -1, -1):
            dp_f[i][j] = max(arr[i]+dp_s[i+1][j], arr[j]+dp_s[i][j-1])
            dp_s[i][j] = min(dp_f[i+1][j], dp_f[i][j-1])

    return max(dp_f[0][n-1], dp_s[0][n-1])

if __name__ == '__main__':
    arr = [4, 7, 9, 5]

    print(func2(arr))