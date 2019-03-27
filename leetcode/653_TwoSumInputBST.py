# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# exist two elements in the BST such that 
# their sum is equal to the given target.
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# Output: True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.values = []
    
    def getValues(self, root: TreeNode):
        if root:
            self.values.append(root.val)
            self.getValues(root.right)
            self.getValues(root.left)
        return self.values
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        lst = self.getValues(root)
        for i, el in enumerate(lst):
            if k - el in lst[:i] + lst[i+1:]:
                return True
        return False
             
            


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findAnagrams("cbaebabacd","abc")
    print(param_1)
