# https://leetcode.com/problems/range-sum-of-bst/
# recursion

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root:
            if L <= root.val <= R:
                return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
            else:
                return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        return 0
