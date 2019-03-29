# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Given two arrays, write a function to compute their intersection.

class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for el in nums1:
            if el in nums2:
                res.append(el)
                nums2.remove(el)
        return res

        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.intersect([1,2,2,1], [2,2])
    print(param_1)
