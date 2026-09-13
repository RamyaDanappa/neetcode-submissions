# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res=[False]
        if root == None:
            return False
        def helper(node, targetSum, curr):
            #base
            if node.left == None and node.right== None:
                curr=curr+node.val
                print(curr)
                if curr==targetSum:
                    res[0]=True
                    return
            #recurson
            if node.left != None:
                helper(node.left, targetSum, curr+node.val)
            if node.right!= None:
                helper(node.right, targetSum, curr+node.val)
        helper(root, targetSum, 0)
        return res[0]       