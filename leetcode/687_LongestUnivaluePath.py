# https://leetcode.com/problems/longest-univalue-path/
# Input:
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
# 2
# Input:
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
# 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getSide(self, root: TreeNode) -> int:
        A = 0
        B = 0
        if root:
            if root.right and root.val == root.right.val:
                A = 1 + self.getSide(root.right)
            if root.left and root.val == root.left.val:
                B = 1 + self.getSide(root.left)
        return max(A, B)
                
    def longestUnivaluePath(self, root: TreeNode) -> int:
        length = 0
        if not root: return 0
        
        A = self.longestUnivaluePath(root.right)
        B = self.longestUnivaluePath(root.left)
        
        if root.right and root.left and root.val == root.right.val == root.left.val:
            length = 2 + self.getSide(root.right) + self.getSide(root.left)
        elif root.right and root.val == root.right.val:
            length = 1+ self.getSide(root.right)
        elif root.left and root.val == root.left.val:
            length = 1 + self.getSide(root.left)
        return max(A, B, length)

# better solutionn
class Solution(object):
    def longestUnivaluePath(self, root):
        longest = 0
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest = max(longest, left + right)
            return max(left, right)
        traverse(root)
        return longest