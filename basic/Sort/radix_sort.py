"""
Radix sort

        avg   best  worst
Time: O(n*k)  O(n*k)  O(n*k)
Space: O(n+k)
Stable

"""


def radix_sort(arr):

    if not len(arr):
        return

    max_ = max(arr)
    n_digits = len(str(max_))

    for j in range(n_digits):
        bucket = [[] for i in range(10)]

        for i in range(len(arr)):
            bucket[arr[i]//(10**j)%10].append(arr[i])

        k = 0

        for i in range(10):
            for j in range(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1



if __name__ == '__main__':
    test_case = [3, 15, 2, 0, 5]

    print(test_case)

    radix_sort(test_case)

    print(test_case)
