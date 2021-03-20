"""
One input stack one output stack
Time Complexity: O(n)
Space Complexity: O(1)
"""


class CQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def appendTail(self, value: int) -> None:
        self.input_stack.append(value)

    def deleteHead(self) -> int:
        if not self.output_stack:
            if not self.input_stack:
                return -1
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()