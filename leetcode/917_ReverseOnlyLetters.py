# https://leetcode.com/problems/reverse-only-letters/
# return the "reversed" string where all characters that are not a letter stay in the same place
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = ''
        for ch in S:
            if ch.isalpha():
                letters += ch
        rev = letters[::-1]
        newstr = ''
        for ch in S:
            if ch.isalpha():
                newstr += rev[0]
                rev = rev[1:]
            else:
                newstr += ch
        return newstr

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.reverseOnlyLetters("a-bC-dEf-ghIj")
    print(param_1)
