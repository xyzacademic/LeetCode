"""


"""

def func1(a):

    def process(a, index, results, path):
        if index == len(a):
            results.add(path)
            return

        current_path = path
        process(a, index+1, results, current_path)
        current_path += a[index]
        process(a, index+1, results, current_path)

    results = set()

    process(a, 0, results, '')

    return results


def func2(a):

    if not a or len(a) == 0:
        return ''

    def process(a, index, results):
        if index == len(a):
            results.append(''.join(a))

        visited = [False] * 26
        for j in range(index, len(a)):
            if not visited[ord(a[j]) - ord('a')]:
                visited[ord(a[j]) - ord('a')] = True
                a[index], a[j] = a[j], a[index]
                process(a, index+1, results)
                a[index], a[j] = a[j], a[index]


    results = []

    process([element for element in a], 0, results)

    return results

if __name__ == '__main__':
    a = 'abca'
    results = func1(a)
    print(results)

    results = func2(a)
    print(results)