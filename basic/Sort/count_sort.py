"""
Count sort

        avg   best  worst
Time: O(n+k)  O(n+k)  O(n+k)
Space: O(n+k)
Stable

"""


def count_sort(arr):

    if len(arr) == 0:
        return

    min_ = min(arr)
    max_ = max(arr)

    count_arr = [0] * (max_ - min_ + 1)
    new_arr = [None] * len(arr)

    for num in arr:
        count_arr[num-min_] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for num in arr[::-1]:
        new_arr[count_arr[num-min_]-1] = num
        count_arr[num-min_] -= 1

    return new_arr


if __name__ == '__main__':
    test_case = [3, 15, 2, 0, -1, 5]

    print(test_case)

    test_case = count_sort(test_case)

    print(test_case)

