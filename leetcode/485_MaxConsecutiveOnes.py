# https://leetcode.com/problems/max-consecutive-ones/
# Given a binary array, find the maximum number of consecutive 1s in this array.
# Input: [1,1,0,1,1,1]
# Output: 3

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        # list elments have to be string to perforem .join()
        li = []
        for el in nums:
            li.append(str(el))
        ones = ''.join(li).split("0")

        count = []
        for el in ones:
            count.append(len(el))
        return max(count)

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findMaxConsecutiveOnes([1,1,0,1,1,1])
    print(param_1)