# https://leetcode.com/problems/majority-element/
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

class Solution:
    def majorityElement(self, nums) -> int:
        uniq = list(set(nums))
        count = []
        for el in uniq:
            count.append(nums.count(el))
        for i in range(len(count)):
            if count[i] > len(nums)/2:
                return uniq[i]

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.majorityElement([2,2,1,1,1,2,2])
    print(param_1)

# Wiser solution provided by Leetcode
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]