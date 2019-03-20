# https://leetcode.com/problems/non-decreasing-array/
# check if it could become non-decreasing by modifying at most 1 element.
# Input: [4,2,1]
# Output: False

class Solution:
    def checkPossibility(self, nums) -> bool:
        decrs = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decrs += 1
                index = i
        if decrs > 1:
            return False
        elif decrs == 1:
            if index != 0 and index != len(nums)-2 and nums[index-1] > nums[index+1] and nums[index+2] < nums[index]:
                return False
        return True


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.checkPossibility([3,4,2,3])
    # param_1 = obj.checkPossibility([4,2,3])
    print(param_1)