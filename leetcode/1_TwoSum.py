# https://leetcode.com/problems/two-sum/

# O(n2)
class Solution:
    def twoSum(self, nums, target: int) :
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# hash table O(n)
class Solution:
    def twoSum(self, nums, target: int) :
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            else:
                return [dic[nums[i]], i]


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.twoSum([2, 7, 11, 15], 9)
    print(param_1)
