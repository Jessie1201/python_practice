# https://leetcode.com/problems/add-binary/
# binary value addition

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int('0b'+ a ,2)
        b_int = int('0b'+ b ,2)
        sum_int = a_int + b_int
        sum_bin = bin(sum_int)[2:]
        return sum_bin

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.addBinary("1010", "1011")
    print(param_1)