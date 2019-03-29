# https://leetcode.com/problems/rectangle-overlap/
# Two rectangles overlap if the area of their intersection is positive

class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        if rec1[0] > rec2[0]:
            rec1, rec2 = rec2, rec1
        if rec2[0] < rec1[2]:
            if rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
                return False
            else: return True
        return False


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isRectangleOverlap([0,0,2,2],[1,1,3,3])
    print(param_1)
