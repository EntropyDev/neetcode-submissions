# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            lv = dfs(node.left) 
            rv = dfs(node.right)
            val = lv+rv
            ans = max(ans, val)
            return 1 + max(lv,rv) 
        dfs(root)
        return ans