"""
charge money
"""


def func1(arr, target):
    if not target or len(arr) == 0 or target <= 0:
        return 0

    def process(idx, arr, rest):
        if idx == len(arr):
            return 1 if rest == 0 else 0

        results = 0
        for n_current_coin in range(rest//arr[idx]+1):
            results += process(idx+1, arr, rest-n_current_coin*arr[idx])

        return results

    return process(0, arr, target)


def func2(arr, target):
    if not target or len(arr) == 0 or target < 0:
        return 0

    dp = {}

    def process(idx, arr, rest, dp):
        key = f'{idx}_{rest}'
        if key in dp:
            return dp[key]

        if idx == len(arr):
            dp[key] = 1 if rest == 0 else 0
            return dp[key]

        dp[key] = 0
        for n_current_coin in range(rest//arr[idx]+1):
            dp[key] += process(idx+1, arr, rest-n_current_coin*arr[idx], dp)

        return dp[key]

    process(0, arr, target, dp)

    return dp[f'0_{target}']


def func3(arr, target):
    if not arr or len(arr) == 0 or target < 0:
        return 0

    def process(arr, target):
        n = len(arr)
        dp = [[0 for i in range(target+1)] for j in range(n+1)]
        dp[n][0] = 1

        for idx in range(n-1, -1, -1):
            for rest in range(target+1):
                dp[idx][rest] = dp[idx+1][rest]
                if rest >= arr[idx]:
                    dp[idx][rest] += dp[idx][rest-arr[idx]]

        return dp[0][target]

    return process(arr, target)


def func4(arr, target):
    if not arr or len(arr) == 0 or target < 0:
        return 0

    dp = {}
    n = len(arr)
    dp[f'{n}_0'] = 1

    for idx in range(n-1, -1, -1):
        for rest in range(target+1):
            key1 = f'{idx}_{rest}'
            if key1 not in dp:
                dp[key1] = dp.get(f'{idx+1}_{rest}', 0)
            if rest >= arr[idx]:
                dp[key1] += dp.get(f'{idx}_{rest-arr[idx]}', 0)

    return dp[f'0_{target}']

if __name__ == '__main__':
    arr = [5, 10, 50, 100]
    target = 1000
    print(func4(arr, target))