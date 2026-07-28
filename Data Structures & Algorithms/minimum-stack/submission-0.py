class MinStack:
    # design it around feature of getting minimum element in O(1) time.
    # need to have internal linked list with curMin and prevMin

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # if first push to the stack
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        # if new value smaller we add it to the stack
        elif val <= self.minStack[-1]:
            self.minStack.append(val)
        # if not, we dublicate old value to the stack
        elif val > self.minStack[-1]:
            self.minStack.append(self.minStack[-1])
       
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
