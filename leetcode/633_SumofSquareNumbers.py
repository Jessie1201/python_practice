# https://leetcode.com/problems/sum-of-square-numbers/
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int(math.sqrt(c))+1):
            if int(math.sqrt(c - i**2)) == math.sqrt(c - i**2):
                return True
        return False


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.judgeSquareSum(4)
    print(param_1)