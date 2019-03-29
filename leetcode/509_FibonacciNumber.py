# https://leetcode.com/problems/fibonacci-number/
# get Fibonacci number

class Solution:
    def fib(self, N: int) -> int:
        lst = [0, 1]
        if N == 0 or N == 1: return lst[N]
        else:
            for _ in range(N-1):
                lst.append(lst[-1] + lst[-2])
            return lst[-1]


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.fib(4)
    print(param_1)
