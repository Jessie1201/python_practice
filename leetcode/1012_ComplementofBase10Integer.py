# https://leetcode.com/problems/complement-of-base-10-integer/
# complement of it's binary representation as a base-10 integer.

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)[2:]
        res = ''
        for el in binary:
            res += '1' if el == '0' else '0'
        return int(res,2)
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.bitwiseComplement(5)
    print(param_1)
