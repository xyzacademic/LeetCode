
def Sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        Sort(left)
        Sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            alist[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1

        





if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort(alist)
    print(alist)