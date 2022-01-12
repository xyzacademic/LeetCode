import collections
import heapq

class DualHeap:
    def __init__(self, k):
        self.small = []
        self.large = []
        self.delayed = collections.Counter()
        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            else:
                break

    def make_balance(self):
        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def insert(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.make_balance()

    def erase(self, num):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)

        self.make_balance()

    def get_median(self):
        return -self.small[0] if self.k % 2 == 1 else (-self.small[0]+self.large[0]) / 2

class Solution:
    def median_sliding_window(self, nums, k):
        dh = DualHeap(k)
        for num in nums[:k]:
            dh.insert(num)

        ans = [dh.get_median()]
        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i-k])
            ans.append(dh.get_median())

        return ans