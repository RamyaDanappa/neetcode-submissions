# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        middle=slow

        #reverse from middle
        reverse=None
        while slow:
            new_node=ListNode(slow.val)
            new_node.next=reverse
            reverse=new_node
            slow=slow.next
        
        res =0

        while reverse:
            res = max(res, reverse.val+head.val)
            reverse=reverse.next
            head=head.next
        return res



        