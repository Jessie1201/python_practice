# https://leetcode.com/problems/merge-two-binary-trees/
# Special use of and/or that not return bool
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        # Another solution, also work
        # if t1 or t2:
        #     res = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        #     res.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        #     res.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        #     return res
        # return None
    
        if t1 or t2:
            if t1 and t2:
                t1.val += t2.val
                t1.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
                t1.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
            elif t2:
                t1 = t2
            return t1
        return None
