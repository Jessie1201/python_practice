# https://leetcode.com/problems/univalued-binary-tree/
# Return true if and only if the given tree is univalued.

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            if root.left:
                if root.val != root.left.val: return False
            if root.right:
                if root.val != root.right.val: return False
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return True
