"""
Queue

"""


class Queue(object):
    def __init__(self):
        self.elements = []

    def is_empty(self):

        return len(self.elements) == 0

    def enqueue(self, val=None):
        if val is not None:
            self.elements.append(val)

        return

    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)

