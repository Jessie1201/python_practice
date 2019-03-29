# https://leetcode.com/problems/reverse-string-ii/
# reverse the first k characters for every 2k characters

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k >= len(s):
            return s[::-1]
        i = 0
        while k*i < len(s):
            s = s[:k*i] + s[k*i:k*(i+1)][::-1] + s[k*(i+1):]
            i += 2
        return s
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.reverseStr("abcdefg", 2)
    print(param_1)
