# https://leetcode.com/problems/binary-search/
# If target exists, then return its index, otherwise return -1.

class Solution:
    def search(self, nums, target: int) -> int:
        return nums.index(target) if target in nums else -1

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.search([-1,0,3,5,9,12], 9)
    print(param_1)
