# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# return the bottom-up level order traversal of its nodes' values
# Typical BFS, for left & right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            thislevel = [root]
            while thislevel:
                row = []
                nextlevel = []
                for node in thislevel:
                    row.append(node.val)
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                res.append(row)
                thislevel = nextlevel
        return res[::-1]