class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        value = self.map.get(key, -1)
        if value == -1:
            return value
        else:
            self.move_node(key)
            return value.value

    def put(self, key: int, value: int) -> None:

        if key in self.map:
            self.map[key].value = value
            self.move_node(key)
        else:
            if len(self.map) == self.capacity:
                self.delete()
            self.insert(key, value)

    def move_node(self, key):
        """
        move node(key) to the position before tail
        """
        node = self.map[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def delete(self, ):

        self.map.pop(self.head.next.key)
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

    def insert(self, key, value):
        node = Node(key, value)
        self.map[key] = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    """

    head <-> node <-> tail
        low        high


    """