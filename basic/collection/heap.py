"""
Binary heap
"""


class MinHeap(object):
    def __init__(self):
        self.heap_size = 0
        self.heap_list = [0]

    def insert(self, value):
        self.heap_list.append(value)
        self.heap_size += 1
        self._perc_up(self.heap_size)

    def pop(self):
        temp = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        self.heap_size -= 1
        self._heapify(1)

        return temp


    def _perc_up(self, i):
        while i > 1:
            if self.heap_list[i] < self.heap_list[i>>1]:
                self.swap(i, i>>1)
            i = i >> 1

    def _heapify(self, i):
        while i<<1 <= self.heap_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.swap(i, mc)
            i = mc

    def min_child(self, i):
        idx = i << 1
        if idx +1 > self.heap_size:
            return idx

        return idx if self.heap_list[idx] < self.heap_list[idx+1] else idx+1

    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

    def build_heap(self, arr):
        self.heap_size = len(arr)
        self.heap_list = [0] + arr
        i = self.heap_size >> 1
        while i > 0:
            self._heapify(i)
            i = i - 1

    def sort(self, arr):
        self.build_heap(arr)
        while self.heap_size > 1:
            self.swap(1, self.heap_size)
            self.heap_size -= 1
            self._heapify(1)


class MaxHeap(object):
    def __init__(self):
        self.heap_list = [0]

    def push(self, val):
        self.heap_list.append(val)
        self.heap_list[0] += 1
        self.perc_up(self.heap_list[0])

        return

    def pop(self, ):
        if self.heap_list[0] == 0:
            print('Heap is empty')
            return
        if self.heap_list[0] == 1:
            self.heap_list[0] -= 1
            return self.heap_list.pop()

        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list.pop()
        self.heap_list[0] -= 1
        self.perc_down(1)
        return val

    def perc_down(self, idx):
        while idx << 1 <= self.heap_list[0]:
            mc = self.max_children(idx)
            if self.heap_list[idx] < self.heap_list[mc]:
                self.swap(idx, mc)
            idx = mc
        return

    def perc_up(self, idx):
        while idx > 1:
            j = idx >> 1
            if self.heap_list[idx] > self.heap_list[j]:
                self.swap(idx, j)
            idx = j

    def swap(self, i, j):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]

        return

    def max_children(self, idx):
        idx = idx << 1
        if idx == self.heap_list[0]:
            return idx

        if self.heap_list[idx] > self.heap_list[idx+1]:
            return idx
        else:
            return idx + 1

    def build_heap(self, arr):
        self.heap_list += arr
        self.heap_list[0] = len(arr)
        idx = self.heap_list[0] >> 1
        while idx > 0:
            self.perc_down(idx)
            idx -= 1

        return

    def sort(self, arr):
        self.build_heap(arr)
        while self.heap_list[0] > 1:
            self.swap(1, self.heap_list[0])
            self.heap_list[0] -= 1
            self.perc_down(1)




if __name__ == '__main__':
    arr = [9, 6, 5, 2, 3, 4, 7]
    heap = MinHeap()
    heap.build_heap(arr)
    print(heap.heap_list)
    heap = MaxHeap()
    heap.build_heap(arr)
    print(heap.heap_list)
    heap = MinHeap()
    heap.sort(arr)
    print(heap.heap_list)
    heap = MaxHeap()
    heap.sort(arr)
    print(heap.heap_list)