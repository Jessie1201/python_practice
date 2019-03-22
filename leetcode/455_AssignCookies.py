# https://leetcode.com/problems/assign-cookies/
# maximize the number of your content children

class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in g:
            for j in s:
                if j >= i:
                    res += 1
                    s.remove(j)
                    break
        return res

        
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findContentChildren([1,2,2,6], [1,2,3,4])
    print(param_1)
