# https://leetcode.com/problems/add-to-array-form-of-integer/
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A = [str(el) for el in A]
        res = list(str(int(''.join(A)) + K))
        res = [int(el) for el in res]
        return res

