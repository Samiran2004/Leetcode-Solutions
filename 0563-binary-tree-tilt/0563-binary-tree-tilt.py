# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.totalTilt = 0

        def getSum(node):
            if not node:
                return 0
            
            leftSum = getSum(node.left)
            rightSum = getSum(node.right)

            self.totalTilt += abs(leftSum - rightSum)

            return node.val + leftSum + rightSum
        
        getSum(root)

        return self.totalTilt