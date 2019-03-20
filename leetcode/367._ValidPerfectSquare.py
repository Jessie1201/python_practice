# https://leetcode.com/problems/valid-perfect-square/
# Given a positive integer num, write a function which returns True if num
# is a perfect square else False.
# Note: Do not use any built-in library function such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        perfect = False
        i = 1
        while i**2 < num:
            i += 1
        if i**2 == num:
            perfect = True
        return perfect

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isPerfectSquare(1)
    print(param_1)