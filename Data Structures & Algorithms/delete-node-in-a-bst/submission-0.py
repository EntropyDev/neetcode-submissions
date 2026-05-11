# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return node
            if key > node.val:
                node.right = dfs(node.right)
            elif key < node.val:
                node.left = dfs(node.left)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                cur = node.right
                while cur.left:
                    cur = cur.left
                cur.left = node.left
                res = node.right
                del node
                return res

            return node

        return dfs(root)                
            
