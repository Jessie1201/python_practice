# https://leetcode.com/problems/rotate-array/
# rotate the array to the right by k steps

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = nums.copy()
        for i in range(len(res)):
            j = (i + k) % len(res)
            nums[j] = res[i]
        # return nums


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.rotate([1,2,3,4,5,6,7], 3)
    print(param_1)
