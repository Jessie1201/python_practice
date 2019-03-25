# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# find the minimum absolute difference between values of any two nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.values = []
        
    def collectVal(self, root: TreeNode):
        if root:
            self.values.append(root.val)
            self.collectVal(root.right)
            self.collectVal(root.left)
        
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.collectVal(root)
        self.values.sort()
        minimun = self.values[1] - self.values[0]
        for i in range(1, len(self.values)-1):
            minimun = min(minimun, self.values[i+1] - self.values[i])
                    
        return minimun
