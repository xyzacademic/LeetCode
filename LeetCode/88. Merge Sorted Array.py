class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1 2 3 3 5 6

        left_pointer = m - 1
        right_pointer = n - 1
        p = m + n - 1

        while left_pointer > -1 or right_pointer > -1:

            if left_pointer == -1:
                nums1[p] = nums2[right_pointer]
                right_pointer -= 1

            elif right_pointer == -1:
                nums1[p] = nums1[left_pointer]
                left_pointer -= 1

            elif nums1[left_pointer] > nums2[right_pointer]:
                nums1[p] = nums1[left_pointer]
                left_pointer -= 1

            else:
                nums1[p] = nums2[right_pointer]
                right_pointer -= 1
            p -= 1