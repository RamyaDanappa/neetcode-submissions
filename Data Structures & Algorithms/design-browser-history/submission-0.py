class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        new_node = Node(url)

        self.current.right = new_node
        new_node.left = self.current
        self.current = new_node

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.left:
            self.current = self.current.left
            steps -= 1

        return self.current.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.right:
            self.current = self.current.right
            steps -= 1

        return self.current.val