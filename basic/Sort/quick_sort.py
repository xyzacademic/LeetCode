"""
insert sort

        avg   best  worst
Time: O(nlogn)  O(nlogn)  O(n^2)
Space: O(logn)
Unstable

"""
import random


# def quick_sort(array):
#     sort_(array, 0, len(array) - 1)
#
#
# def sort_(array, left_bound, right_bound):
#     if left_bound >= right_bound:
#         return
#
#     mid = partition(array, left_bound, right_bound)
#
#     sort_(array, left_bound, mid - 1)
#     sort_(array, mid + 1, right_bound)
#
#     return
#
#
# def partition(array, left_bound, right_bound):
#     pivot_idx = random.randint(left_bound, right_bound)
#     array[pivot_idx], array[left_bound] = array[left_bound], array[pivot_idx]
#     pivot = array[left_bound]
#
#     left_pointer = left_bound + 1
#     right_pointer = right_bound
#
#     while left_pointer <= right_pointer:
#         while left_pointer <= right_pointer and array[left_pointer] >= pivot:
#             left_pointer += 1
#
#         while left_pointer <= right_pointer and array[right_pointer] < pivot:
#             right_pointer -= 1
#
#         if left_pointer < right_pointer:
#             array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
#
#     array[right_pointer], array[left_bound] = array[left_bound], array[right_pointer]
#
#     # print(array)
#     # print(right_pointer)
#     return right_pointer

def quick_sort(array):
    sort_(array, 0, len(array)-1)

def sort_(array, left, right):
    if left >= right:
        return

    mid = partition(array, left, right)

    sort_(array, left, mid-1)
    sort_(array, mid+1, right)

    return

def partition(array, left_bound, right_bound):

    pivot_idx = random.randint(left_bound, right_bound)
    pivot = array[pivot_idx]
    array[right_bound], array[pivot_idx] = array[pivot_idx], array[right_bound]

    left = left_bound
    right = right_bound - 1

    while left <= right:
        while left <= right and array[right] >= pivot:
            right -= 1

        while left <= right and array[left] < pivot:
            left += 1

        if left < right:
            array[left], array[right] = array[right], array[left]

    array[right_bound], array[left] = array[left], array[right_bound]

    return left



if __name__ == '__main__':
    test_case = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5]


    print(test_case)

    quick_sort(test_case)

    print(test_case)


