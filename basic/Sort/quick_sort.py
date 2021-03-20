"""
insert sort

        avg   best  worst
Time: O(nlogn)  O(nlogn)  O(n^2)
Space: O(logn)
Unstable

"""


def quick_sort(arr):

    if not len(arr):
        return

    sort_(arr, 0, len(arr)-1)

    return


def sort_(arr, left_bound, right_bound):

    # check
    if left_bound >= right_bound:
        return

    # get the pivot index
    mid = partition(arr, left_bound, right_bound)

    # recursive
    sort_(arr, left_bound, mid-1)
    sort_(arr, mid+1, right_bound)

    return


def partition(arr, left_bound, right_bound):

    # init pivot
    pivot = arr[right_bound]

    left_pointer = left_bound
    right_pointer = right_bound - 1

    while left_pointer <= right_pointer:
        while left_pointer <= right_pointer and arr[left_pointer] <= pivot:
            left_pointer += 1

        while left_pointer <= right_pointer and arr[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer < right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]

    arr[left_pointer], arr[right_bound] = arr[right_bound], arr[left_pointer]

    return left_pointer

if __name__ == '__main__':
    test_case = [3, 15, 2, 0, -1, 5]

    print(test_case)

    quick_sort(test_case)

    print(test_case)
