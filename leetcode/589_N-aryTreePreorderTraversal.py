# https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# return the preorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.res = []
    
    def preorder(self, root: 'Node') -> List[int]:
        if root:
            self.res.append(root.val)
            for ch in root.children:
                self.preorder(ch)
        return self.res
