
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = []
        length_nums1 = len(nums1)
        length_nums2 = len(nums2)
        i = 0
        j = 0
        # O(n)
        while i < length_nums1 and j < length_nums2:
            if nums1[i] <= nums2[j]:
                num.append(nums1[i])
                i += 1
            else:
                num.append(nums2[j])
                j += 1

        while i < length_nums1:
            num.append(nums1[i])
            i += 1

        while j < length_nums2:
            num.append(nums2[j])
            j += 1

        mid_idx = (i+j) >> 1
        # print(num)
        # print(i+j)
        # print(mid_idx)
        if (i+j)&1:
            return num[mid_idx]
        else:
            return (num[mid_idx]+num[mid_idx-1])/2












if __name__ == '__main__':
    case1 = [[1, 3],
             [2]]

    case2 = [[1, 2],
             [3, 4]]


    s = Solution()
    print(f'Case 1 {s.findMedianSortedArrays(case1[0], case1[1]) == 2}')
    print(f'Case 2 {s.findMedianSortedArrays(case2[0], case2[1]) == 2.5}')