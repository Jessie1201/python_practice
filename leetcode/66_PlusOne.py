# https://leetcode.com/problems/plus-one/
# array of digits representing a non-negative integer, plus one to the integer.

class Solution:
    def plusOne(self, digits):
        digits = [str(el) for el in digits]
        res = list(str(int(''.join(digits)) + 1))
        res = [int(el) for el in res]
        return res
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.plusOne([1,2,3])
    print(param_1)
