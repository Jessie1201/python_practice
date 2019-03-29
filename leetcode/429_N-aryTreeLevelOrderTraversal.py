# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# the level order traversal of its nodes' values
# Typical BFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root:
            thislevel = [root]
            while thislevel:
                row = []
                for node in thislevel:
                    row.append(node.val)
                res.append(row)
                nextlevel = [child for node in thislevel for child in node.children if child]
                thislevel = nextlevel
        return res

