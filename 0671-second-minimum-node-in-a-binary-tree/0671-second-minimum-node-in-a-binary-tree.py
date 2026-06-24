# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first = root.val
        sec = float('inf')

        def dfs(node):
            nonlocal sec

            if node is None:
                return
            
            if first < node.val < sec:
                sec = node.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)

        if sec != float('inf'):
            return sec
        else:
            return -1