"""
Bubble sort

        avg   best  worst
Time: O(n^2)  O(n)  O(n^2)
Space: O(1)
Stable

"""


def bubble_sort(arr):

    if len(arr) == 0:
        return

    count_swap = 0
    for last_idx in range(len(arr)-1, 0, -1):
        for i in range(last_idx):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap += 1

        if not count_swap:
            break


if __name__ == '__main__':
    test_case = [3, 15, 2, 0, -1, 5]

    print(test_case)

    bubble_sort(test_case)

    print(test_case)

