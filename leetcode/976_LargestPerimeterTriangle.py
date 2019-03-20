# https://leetcode.com/problems/largest-perimeter-triangle/
# Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
# If it is impossible to form any triangle of non-zero area, return 0.

class Solution:
    def largestPerimeter(self, A) -> int:
        if len(A) < 3:
            return 0
        A.sort()
        ordered = A[::-1]
        i = 0
        while (ordered[i] >= ordered[i+1] + ordered[i+2]):
            i += 1
            if i > len(ordered)-3:
                return 0
        return ordered[i] + ordered[i+1] + ordered[i+2]

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.largestPerimeter([1,2,1])
    print(param_1)