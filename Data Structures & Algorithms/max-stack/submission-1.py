from _heapq import heapify
import heapq
class MaxStack:

    def __init__(self):
        self.stack=[]
        self.heap=[]

    def push(self, x: int) -> None:
        if x != None:
            self.stack.append(x)
            heapq.heappush(self.heap, -x)

    def pop(self) -> int:
        pop_val = self.stack.pop()
        self.heap.remove(-pop_val)
        heapq.heapify(self.heap)
        return pop_val

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return -self.heap[0]

    def popMax(self) -> int:
        max_val = -heapq.heappop(self.heap)

        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i] == max_val:
                del self.stack[i]
                break
        return max_val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
