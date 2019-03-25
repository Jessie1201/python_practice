# https://leetcode.com/problems/buddy-strings/
# swap two letters in A so that the result equals B.

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        A, B = list(A), list(B)
        diff = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff.append(i)
        if not diff:
            return len(set(A)) < len(A)
        if len(diff) != 2:
            return False
        A[diff[0]], A[diff[1]] = A[diff[1]], A[diff[0]]
        
        return A == B
        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.buddyStrings("aab","aab")
    print(param_1)
