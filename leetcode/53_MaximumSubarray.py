# https://leetcode.com/problems/maximum-subarray/
# DIFFICULT - find the contiguous subarray (containing at least one number) which has the largest sum
# refered others' solution

class Solution:
    def maxSubArray(self, nums) -> int:
        curSum = maxSum = nums[0]
        for el in nums[1:]:
            curSum = max(el, curSum + el)
            maxSum = max(maxSum, curSum)
        return maxSum

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    # param_1 = obj.maxSubArray([-2,1])
    print(param_1)
