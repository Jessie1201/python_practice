# https://leetcode.com/problems/set-mismatch/
# find the number occurs twice and then find the number that is missing
# (el in Dic) is way quicker than (el in list)

import collections
class Solution:
    def findErrorNums(self, nums):
        res = []
        count = collections.Counter(nums)
        for key in count:
            if count[key] == 2:
                res.append(key)
        correct = list(range(1,len(nums)+1))
        for el in correct:
            if not el in count:
                res.append(el)
        return res
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.findErrorNums([1,2,2,4])
    print(param_1)
