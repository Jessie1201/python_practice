# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# longest continuous increasing subsequence (subarray).

class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        if not nums:
            return 0
        if all(nums[i] >= nums[i+1] for i in range(len(nums)-1)):
            return 1

        cont = []
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1] and (i == 0 or nums[i-1] >= nums[i]):
                for j in range(i+1, len(nums)-1):
                    if nums[j] >= nums[j+1]:
                        cont.append([i,j])
                        break
                    elif j == len(nums)-2:
                        cont.append([i,j+1])
        if not cont:
            return 2
        return max([el[1] - el[0] + 1 for el in cont])

        
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findLengthOfLCIS([1,2])
    print(param_1)
