class TreeNode:
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root=TreeNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=TreeNode()
            curr=curr.children[ch]
        curr.word=True
        

    def search(self, word: str) -> bool:
        def dfs(index, curr):

            if index == len(word):
                return curr.word

            ch = word[index]

            # Normal character
            if ch != ".":
                if ch not in curr.children:
                    return False

                return dfs(index + 1, curr.children[ch])

            # '.': try every child
            for child in curr.children.values():
                if dfs(index + 1, child):
                    return True

            return False

        return dfs(0, self.root)

        
