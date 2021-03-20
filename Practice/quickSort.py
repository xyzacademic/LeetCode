
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        while alist[leftmark] <= pivotvalue and leftmark <= rightmark:
            leftmark += 1

        if rightmark < leftmark:
            done = True

        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark






if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    quickSort(alist)
    print(alist)