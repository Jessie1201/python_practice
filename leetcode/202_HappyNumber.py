# https://leetcode.com/problems/happy-number/
# use of set to hash

class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        history = {num}
        while num != '1':
            num = str(sum([(int(el))**2 for el in num]))
            if num not in history:
                history.add(num)
            else:
                return False
        return True

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isHappy(20)
    print(param_1)