# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        childSet = set()
        nodeMap = {}

        for parent, child, isLeft in descriptions:
            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(parent)
            
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)
            
            if isLeft == 1:
                nodeMap[parent].left = nodeMap[child]
            else:
                nodeMap[parent].right = nodeMap[child]
            
            childSet.add(child)
        
        for parent, child, isLeft in descriptions:
            if parent not in childSet:
                return nodeMap[parent]
        
        return None