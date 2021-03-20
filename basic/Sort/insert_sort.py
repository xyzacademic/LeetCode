"""
insert sort

        avg   best  worst
Time: O(n^2)  O(n)  O(n^2)
Space: O(1)
Stable

"""


def insert_sort(arr):

    if not len(arr):

        return

    for i in range(1, len(arr)):

        while i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return


if __name__ == '__main__':
    test_case = [3, 15, 2, 0, -1, 5]

    print(test_case)

    insert_sort(test_case)

    print(test_case)
