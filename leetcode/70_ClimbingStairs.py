# https://leetcode.com/problems/climbing-stairs/
# either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Difficult - Dynamic Programming

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp = [1, 2]
            i = 3
            while i <= n:
                dp.append(dp[-1] + dp[-2])
                i += 1
            return dp[-1]

# # My org recursive solution, exeeded time
# class Solution:
#     def __init__(self):
#         self.count = 1
#     def climbStairs(self, n: int) -> int:
#         if n >= 2:
#             self.count += 1
#             self.climbStairs(n-1)
#             self.climbStairs(n-2)
#         return self.count

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.climbStairs(35)
    print(param_1)
