from collections import deque

class MyStack:

    def __init__(self):
        # We'll use a single queue
        self.q = deque()

    def push(self, x: int) -> None:
        # Add element to the back
        self.q.append(x)
        # Rotate the queue so that x becomes the front (top of stack)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Remove from front (which is the stack's top)
        return self.q.popleft()

    def top(self) -> int:
        # Peek at the front
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
