# https://leetcode.com/problems/sort-an-array/
# quick sort and bubble sort

class Solution:
    # bubble sort
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
    
    # quick sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            small = []
            pivot = []
            big = []
            for el in nums:
                if el > nums[-1]:
                    big.append(el)
                elif el < nums[-1]:
                    small.append(el)
                else:
                    pivot.append(el)
            nums = self.sortArray(small) + pivot + self.sortArray(big)
        return nums


if __name__=="__main__":
    # obj = Solution()
    # param_1 = obj.partitionDisjoint([5,0,3,8,6])
    # print(param_1)
