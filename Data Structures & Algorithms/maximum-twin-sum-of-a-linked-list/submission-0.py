# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        res=[]
        #find the middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middle = slow
        #reverse the second part from the middle
        reverse=None
        while slow:
            new_node=ListNode(slow.val)
            new_node.next=reverse
            reverse=new_node
            slow=slow.next
        #now add and compare between head and reverse
        res =0
        while reverse:
            res=max(res ,reverse.val + head.val)
            reverse=reverse.next
            head=head.next
        return res




   
            
        