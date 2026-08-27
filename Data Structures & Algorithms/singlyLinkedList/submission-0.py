class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = Node(-1)   # dummy head simplifies insert/remove at index 0
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self._node_at(index)
        return node.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = Node(val)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        prev = self.head
        for _ in range(index):
            prev = prev.next
        target = prev.next
        prev.next = target.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def _node_at(self, index: int) -> Node:
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr