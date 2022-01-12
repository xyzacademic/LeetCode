class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []

        table = {}
        for num in nums:
            if num not in table:
                table[num] = 0
            else:
                table[num] += 1

        new_arr = []

        count = 0
        import heapq

        for key, value in table.items():
            if count < k:
                heapq.heappush(new_arr, (value, key))
            else:
                if value > new_arr[0][0]:
                    heapq.heappop(new_arr)
                    heapq.heappush(new_arr, (value, key))

            # if k <= count and value > new_arr[0][0]:
            #     heapq.heappop(new_arr)
            # heapq.heappush(new_arr, (value, key))
            count += 1

        return [num[1] for num in new_arr]
