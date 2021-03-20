'''

'''

class Solution:
    def replaceSpace(self, s: str) -> str:

        return "".join(["%20" if c == ' ' else c for c in s])


if __name__ == '__main__':
    test_case = [
        'We are happy.',

    ]

    solution = Solution()
    for tc in test_case:
        print(solution.replaceSpace(s=tc))
