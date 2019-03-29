# https://leetcode.com/problems/sqrtx/
# Implement int sqrt(int x).
# binary search

class Solution:
    def mySqrt(self, x: int) -> int:
        border = [0,x]
        i = int(x/2)
        while not i**2 <= x < (i+1)**2:
            if i**2 > x:
                border[1] = i
            elif (i+1)**2 <= x:
                border[0] = i+1
            i = int((border[1]+border[0])/2)
        return i
            
        
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.mySqrt(100)
    print(param_1)
