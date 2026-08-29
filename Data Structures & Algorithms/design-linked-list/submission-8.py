class ListNode:
    def __init__(self, val):
        self.val=val
        self.prev=None
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=ListNode(-1)
       
    def get(self, index: int) -> int:

        current=self.head.next
        count = 0

        while current:
            if count ==index:
                return current.val
            current=current.next
            count+=1
        return -1

        

    def addAtHead(self, val: int) -> None:
        new_node=ListNode(val)
    
        new_node.next=self.head.next
        new_node.prev=self.head
        if self.head.next:
            self.head.next.prev=new_node
        self.head.next=new_node
          

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        current = self.head
        while current.next != None:
            current=current.next
        
        current.next=new_node
        new_node.prev=current

        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node=ListNode(val)
        current = self.head
        count =0
        while current.next != None:
            if count == index:
                
                new_node.prev=current
                new_node.next=current.next
                current.next.prev=new_node
                current.next=new_node
                return
            count+=1
            current=current.next
        if count == index:
            new_node.prev = current
            current.next = new_node

            
    def deleteAtIndex(self, index: int) -> None:

        count =0
        current = self.head.next

        while current:
            if count == index:
                 
                current.prev.next = current.next
                if current.next:
                   
                    current.next.prev=current.prev
                return
            count+=1
            current=current.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)