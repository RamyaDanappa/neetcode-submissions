# Definition for a binary tree node.
# class TreeNode:
from types import resolve_bases
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res=[]
        def helper(node, res):
            if not node:
                return
            helper(node.left, res)
            res.append(node.val)
            helper(node.right, res)
        helper(root, res)
        return res


        