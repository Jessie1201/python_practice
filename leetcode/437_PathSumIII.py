# https://leetcode.com/problems/path-sum-iii/
# Find the number of paths that sum to a given value.
# Example:
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# Return 3. The paths that sum to 8 are:
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSumNode(self, root: TreeNode, sum: int) -> int:
        if root:
            return int(root.val == sum) + self.pathSumNode(root.left, sum-root.val) + self.pathSumNode(root.right, sum-root.val)
        return 0
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root:
            return self.pathSumNode(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0