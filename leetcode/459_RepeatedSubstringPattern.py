
# https://leetcode.com/problems/repeated-substring-pattern/
# check if it can be constructed by taking a substring of it
# and appending multiple copies

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, int(len(s)/2)+1):
            if s == '' + s[:i] * int(len(s)/i):
                return True
        return False
        
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.repeatedSubstringPattern("abab")
    print(param_1)
