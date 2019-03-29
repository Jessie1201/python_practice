# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# Output: [8,6,2,4]
# Explanation: 
# At the beginning, the array is [1,2,3,4].
# After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
# After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.

class Solution:
    def sumEvenAfterQueries(self, A, queries):
        res = [sum([num for num in A if num % 2 == 0])]
        for el in queries:
            if el[0]%2==1 and A[el[1]]%2==1:
                res.append(res[-1]+el[0]+A[el[1]])
            elif el[0]%2==1 and A[el[1]]%2==0:
                res.append(res[-1]-A[el[1]])
            elif el[0]%2==0 and A[el[1]]%2==0:
                res.append(res[-1]+el[0])
            else:
                res.append(res[-1])
            A[el[1]] += el[0]
        return res[1:]
        


if __name__=="__main__":
    obj = Solution()
    param_1 = obj.sumEvenAfterQueries([1],[[4,0]])
    print(param_1)
