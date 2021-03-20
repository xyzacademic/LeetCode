"""
merge sort

        avg   best  worst
Time: O(nlogn)  O(nlogn)  O(nlogn)
Space: O(n)
Stable

"""


def merge_sort(arr):

    if not len(arr):
        return

    split_and_merge(arr, 0, len(arr)-1)

    return


def split_and_merge(arr, left_bound, right_bound):

    # check
    if left_bound >= right_bound:
        return

    mid = (left_bound + right_bound) // 2
    split_and_merge(arr, left_bound, mid)
    split_and_merge(arr, mid+1, right_bound)

    # merge

    left_arr = arr[left_bound:mid+1]
    right_arr = arr[mid+1:right_bound+1]

    i = 0
    j = 0
    k = left_bound

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return





if __name__ == '__main__':
    test_case = [3, 15, 2, 0, -1, 5]

    print(test_case)

    merge_sort(test_case)

    print(test_case)
