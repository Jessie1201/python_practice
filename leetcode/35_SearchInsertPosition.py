# https://leetcode.com/problems/search-insert-position/
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif all(el < target for el in nums):
            return len(nums)
        elif all(el > target for el in nums):
            return 0
        for i in range(len(nums)):
            if nums[i] < target < nums[i+1]:
                return i + 1
        
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.searchInsert([1,3,5,6], 4)
    print(param_1)
