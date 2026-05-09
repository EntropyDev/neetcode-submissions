# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            lv = dfs(node.left)
            rv = dfs(node.right)
            if abs(lv-rv) > 1:
                res = False
            return 1 + max(lv,rv)
        
        dfs(root)
        return res
