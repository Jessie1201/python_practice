# https://leetcode.com/problems/binary-number-with-alternating-bits/
# whether it has alternating bits
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = bin(n)[2:]
        return all(bit[i] != bit[i+1] for i in range(len(bit)-1))
        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.hasAlternatingBits(7)
    print(param_1)
