class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.assist_stack = [inf]

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        self.assist_stack.append(min(self.assist_stack[-1], val))

    def pop(self) -> None:
        self.main_stack.pop()
        self.assist_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.assist_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()