"""
Stack
"""


class Stack(object):
    def __init__(self):
        self.elements = []

    def is_empty(self, ):

        return len(self.elements) == 0

    def peek(self):

        return self.elements[-1]

    def push(self, val=None):
        if val is not None:
            self.elements.append(val)

        return

    def pop(self):

        return self.elements.pop()
