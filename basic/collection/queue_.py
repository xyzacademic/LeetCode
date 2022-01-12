


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Queue(object):
#     """
#     ListNode
#     """
#     def __init__(self):
#         self.size = 0
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next = self.tail
#         self.tail.next = self.head
#
#     def push(self, val):
#         node = ListNode(val)
#         self.tail.next.next = node
#         node.next = self.tail
#         self.tail.next = node
#         self.size += 1
#         return
#
#     def pop(self, ):
#         if self.size == 0:
#             return None
#         node = self.head.next
#         self.head.next = node.next
#         self.size -= 1
#         if self.size == 0:
#             self.tail.next = self.head
#         val = node.val
#         del node
#         return val
#
#     def __len__(self):
#         return self.size


class Queue(object):

    """
    Queue array
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.array = [None] * self.max_size
        self.head = 0
        self.tail = 0

    def get_mod(self, idx):
        return (idx + self.max_size) % self.max_size

    def push(self, val):
        self.array[self.tail] = val
        self.tail = self.get_mod(self.tail+1)
        if self.tail == self.head:
            self.expand()
        return

    def expand(self):
        new_array = [None] * self.max_size * 2

        k = 0
        for i in range(self.head, self.max_size):
            new_array[k] = self.array[i]
            k += 1

        for i in range(self.head):
            new_array[k] = self.array[i]
            k += 1
        self.array = new_array
        self.head = 0
        self.tail = k
        self.max_size *= 2

    def pop(self, ):
        val = self.array[self.head]
        self.array[self.head] = None
        self.head = self.get_mod(self.head+1)
        return val


    def __len__(self):
        return len(self.array)


if __name__ == '__main__':
    a = [0, 1, 3, 5]
    print(a)
    queue = Queue(4)
    for val in a:
        queue.push(val)
        continue

    print(len(queue))