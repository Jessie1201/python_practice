#https://leetcode.com/problems/pascals-triangle-ii/
#  return the kth index row of the Pascal's triangle.

class Solution:
    def getRow(self, rowIndex: int):
        if rowIndex >= 1:
            pre_row = self.getRow(rowIndex-1)
            this_row = [1]
            for i in range(len(pre_row) - 1):
                this_row.append(pre_row[i] + pre_row[i+1])
            this_row.append(1)
            return this_row
        return [1]
        

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.getRow(3)
    print(param_1)
