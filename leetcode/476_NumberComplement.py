# https://leetcode.com/problems/number-complement/
# output complement number

class Solution:
    def findComplement(self, num: int) -> int:
        bin_in = bin(num)
        bin_out = "0b"
        for el in bin_in[2:]:
            bin_out += "1" if el == "0" else "0"
        return int(bin_out,2)
        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findComplement(5)
    print(param_1)
