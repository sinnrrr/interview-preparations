import math


class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(
            min(val, self.min_stack[-1] if self.min_stack else math.inf)
        )
        self.stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def test():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    assert obj.getMin() == -3
    obj.pop()
    assert obj.top() == 0
    assert obj.getMin() == -2
