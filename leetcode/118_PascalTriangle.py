# https://leetcode.com/problems/pascals-triangle/
# generate the first numRows of Pascal's triangle.
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        else:
            res = [[1]]
            i = 2
            row = [1]
            while i <= numRows:
                segA = row[:]
                segB = row[:]
                segA.append(0)
                segB.insert(0,0)
                row = [segA[i] + segB[i] for i in range(len(segA))]
                res.append(row)
                i += 1
            return res

        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.generate(5)
    print(param_1)
