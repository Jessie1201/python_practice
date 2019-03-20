# https://leetcode.com/problems/trim-a-binary-search-tree/
# trim the tree so that all its elements lies in [L, R]
# Input: 
#     1
#    / \
#   0   2
#   L = 1
#   R = 2
# Output: 
#     1
#       \
#        2
# Input: 
#     3
#    / \
#   0   4
#    \
#     2
#    /
#   1
#   L = 1
#   R = 3
# Output: 
#       3
#      / 
#    2   
#   /
#  1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root:
            if root.val < L:
                root = root.right
                root = self.trimBST(root, L, R)
            elif root.val > R:
                root = root.left
                root = self.trimBST(root, L, R)
            else:
                root.right = self.trimBST(root.right, L, R)
                root.left = self.trimBST(root.left, L, R)
            return root
