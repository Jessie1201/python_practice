# https://leetcode.com/problems/palindrome-number/
# whether an integer is a palindrome

class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]
        return str(x) == rev


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isPalindrome(-121)
    print(param_1)
