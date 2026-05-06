class MinStack:

    def __init__(self):
        self.min_value = deque()
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp = min(self.min_value[-1], val) if self.min_value else val
        self.min_value.append(temp)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]