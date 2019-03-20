# https://leetcode.com/problems/sort-array-by-parity/
# Given an array A of non-negative integers, return an array consisting 
# of all the even elements of A, followed by all the odd elements of A.

class Solution:
    def sortArrayByParity(self, A):
        result = []
        for el in A:
            if el % 2 == 0:
                result.insert(0, el)
            else:
                result.append(el)
        return result

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.sortArrayByParity([3,1,2,4])
    print(param_1)