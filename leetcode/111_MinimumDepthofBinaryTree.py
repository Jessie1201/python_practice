# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Given a binary tree, find its minimum depth.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        chil = [self.minDepth(root.right), self.minDepth(root.left)]
        if set(chil) == {0}:
            d = 1
        else:
            d = 1 + min(i for i in chil if i != 0)
        return d
        
