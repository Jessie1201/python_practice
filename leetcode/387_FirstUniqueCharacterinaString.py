# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.
# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] not in s[:i] + s[i+1:]:
                return i
        return -1
            

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.firstUniqChar("loveleetcode")
    print(param_1)