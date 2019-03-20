# https://leetcode.com/problems/letter-case-permutation/
# DIFFICULT - below is referenced from others' solution
# Backtracking: transform every letter individually to be lowercase or uppercase

class Solution:
    def letterCasePermutation(self, S: str):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.letterCasePermutation("A1b2c")
    print(param_1)
