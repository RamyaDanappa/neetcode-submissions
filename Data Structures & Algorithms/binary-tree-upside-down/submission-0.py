
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root):
            if not root or not root.left:
                return root

            new_root = dfs(root.left)

            root.left.left = root.right
            root.left.right = root

            root.left = None
            root.right = None

            return new_root

        return dfs(root)
