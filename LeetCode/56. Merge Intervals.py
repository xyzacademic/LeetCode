class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals or len(intervals) == 0 or intervals == [[]]:
            return [[]]

        intervals.sort(key=lambda x: x[0])

        results = []

        for interval in intervals:
            if not results or interval[0] > results[-1][1]:
                results.append(interval)
            else:
                results[-1][1] = max(interval[1], results[-1][1])

        return results