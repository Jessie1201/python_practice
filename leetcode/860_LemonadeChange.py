# https://leetcode.com/problems/lemonade-change/
# Return true if and only if you can provide every customer with correct change.

class Solution:
    def lemonadeChange(self, bills) -> bool:
        five = ten = 0
        for el in bills:
            if el == 5:
                five += 1
            elif el == 10:
                if five == 0:
                    return False
                else:
                    five -= 1
                    ten += 1
            elif el == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.lemonadeChange([5,5,5,10,20])
    print(param_1)