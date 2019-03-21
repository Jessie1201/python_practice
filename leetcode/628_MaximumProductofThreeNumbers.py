# https://leetcode.com/problems/maximum-product-of-three-numbers/
# find three numbers whose product is maximum

class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        if all(el >= 0 for el in nums) or all(el <= 0 for el in nums) or len([el for el in nums if el < 0]) == 1:
            return nums[-1] * nums[-2] * nums[-3]
        # Have both negative and positive, and at least 2 negatives
        else:
            return max(nums[-2] * nums[-3], nums[0] * nums[1]) * nums[-1]

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.maximumProduct([-4,-3,-2,-1,1])
    print(param_1)
