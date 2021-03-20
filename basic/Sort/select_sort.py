"""
select sort

        avg   best  worst
Time: O(n^2)  O(n^2)  O(n^2)
Space: O(1)
Unstable

"""


def select_sort(arr):

    if not len(arr):
        return

    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]


    return

if __name__ == '__main__':
    test_case = [3, 15, 2, 0, -1, 5]

    print(test_case)

    select_sort(test_case)

    print(test_case)
