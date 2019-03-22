# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# convert sorted list to a height balanced BST.
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5],
# which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        else:
            root = TreeNode(nums[int(len(nums)/2)])
            left = nums[:int(len(nums)/2)]
            right = nums[int(len(nums)/2)+1:]
            
            root.left = self.sortedArrayToBST(left)
            root.right = self.sortedArrayToBST(right)

            return root
