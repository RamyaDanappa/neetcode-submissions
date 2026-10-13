import heapq

class MaxStack:
    def __init__(self):
        self.stack = []
        self.heap = []    # store -x so the min-heap behaves as a max-heap

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.heap, -x)

    def pop(self) -> int:
        x = self.stack.pop()
        self.heap.remove(-x)       # remove one copy of x from the heap
        heapq.heapify(self.heap)   # restore the heap property
        return x

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return -self.heap[0]

    def popMax(self) -> int:
        mx = -heapq.heappop(self.heap)
        # remove the top-most occurrence of mx from the stack
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == mx:
                del self.stack[i]
                break
        return mx