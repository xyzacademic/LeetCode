class ListNode(object):
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque(object):
    def __init__(self):
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, val):
        node = ListNode(val, self.tail, self.tail.prev)
        self.size += 1
        self.tail.prev.next = node
        self.tail.prev = node

        return

    def append_left(self, val):
        node = ListNode(val, self.head.next, self.head)
        self.size += 1
        self.head.next.prev = node
        self.head.next = node
        return

    def pop(self):
        if self.size < 1:
            raise ValueError('deque is empty')

        self.size -= 1
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev

        return node.val


    def popleft(self):
        if self.size < 1:
            raise ValueError('deque is empty')

        self.size -= 1
        node = self.head.next
        node.next.prev = self.head
        self.head.next = node.next

        return node.val





class DequeArray(object):
    def __init__(self, n):
        self.max_size = n
        self.array = [None] * n
        self.head = 0
        self.tail = 0

    def _expand(self):
        new_array = [None] * self.max_size * 2

        i = 0
        for j in range(self.head, self.max_size):
            new_array[i] = self.array[j]
            i += 1

        for j in range(self.head):
            new_array[i] = self.array[j]
            i += 1

        self.head = 0
        self.tail = self.max_size
        self.max_size *= 2

    def push_left(self, val):
        self.head = self._get_mod(self.head-1)
        self.array[self.head] = val
        if self.head == self.tail:
            self._expand()

    def push_right(self, val):
        self.array[self.tail] = val
        self.tail = self._get_mod(self.tail+1)
        if self.head == self.tail:
            self._expand()

    def pop_left(self):
        val = self.array[self.head]
        self.array[self.head] = None
        self.head = self._get_mod(self.head+1)
        return val

    def pop_right(self):
        self.tail = self._get_mod(self.tail-1)
        val = self.array[self.tail]
        self.array[self.tail] = None
        return val

    def peek_head(self):
        return self.array[self.head]

    def peek_tail(self):
        return self.array[self._get_mod(self.tail-1)]

    def _get_mod(self, idx):
        return (idx + self.max_size) % self.max_size

    def _expand(self, ):
        pass

    def size(self):
        return self._get_mod(self.tail - self.head)

    def is_empty(self):
        return self.head == self.tail

    def clear(self):
        head = self.head
        tail = self.tail

        while head != tail:
            self.array[head] = None
            head = self._get_mod(head + 1)

        self.head = 0
        self.tail = 0