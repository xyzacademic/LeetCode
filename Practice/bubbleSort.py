

def Sort(aList):
    length_aList = len(aList)
    for last in range(length_aList - 1, 0, -1):
        for i in range(last):
            if aList[i] > aList[i + 1]:
                aList[i], aList[i+1] = aList[i+1], aList[i]

    return




if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    Sort(alist)
    print(alist)