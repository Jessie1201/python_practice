# https://leetcode.com/problems/reshape-the-matrix/
# The reshaped matrix need to be filled with all the elements of the original matrix 
# in the same row-traversing order as they were.class Solution:
class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            dig = []
            for row in nums:
                for col in row:
                    dig.append(col)
            reshape = []
            for row in range(r):
                reshape.append(dig[c * row : c * (row+1)])
            return reshape

        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.matrixReshape([[1,2],[3,4]], 4, 1)
    print(param_1)