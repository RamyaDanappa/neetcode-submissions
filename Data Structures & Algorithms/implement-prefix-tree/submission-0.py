class treenode:
    def __init__(self) -> None:  
        self.childern={}
        self.word = False
class PrefixTree:

    def __init__(self):
        self.root=treenode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.childern:
                curr.childern[ch]=treenode()
            curr=curr.childern[ch]
        curr.word=True


    def search(self, word: str) -> bool:
        curr= self.root
        for ch in word:
            if ch not in curr.childern:
                return False
            curr=curr.childern[ch]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr= self.root
        for ch in prefix:
            if ch not in curr.childern:
                return False
            curr=curr.childern[ch]
        return True
        
        
        