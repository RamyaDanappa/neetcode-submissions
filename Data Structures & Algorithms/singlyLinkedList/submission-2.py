class Node:
    def __init__(self,val):
        self.val=val
        self.next = None
class LinkedList:
    
    def __init__(self):
        self.size =0
        self.head= Node(-1)

    
    def get(self, index: int) -> int:
        i=0
        current = self.head.next
        while current != None:
            if i==index:
                return current.val
            current=current.next
            i+=1
        return -1

        

    def insertHead(self, val: int) -> None:
        new_node= Node(val)
        new_node.next=self.head.next
        self.head.next=new_node
        self.size+=1
        

    def insertTail(self, val: int) -> None:
        new_node=Node(val)
        current= self.head
        while current.next != None:
            current=current.next
        current.next=new_node
        new_node.next=None
        self.size+=1
          

    def remove(self, index: int) -> bool:
        if self.size <=index or index < 0 :
            return False
        current = self.head.next
        previous= self.head
        i=0
        while current != None:
            if i==index:
                previous.next= current.next
                self.size -=1
                return True
            i+=1
            previous = current
            current=current.next
            
        

    def getValues(self) -> List[int]:
        res= []
        current = self.head.next
        while current:
            res.append(current.val)
            current=current.next
        return res

        
