# https://leetcode.com/problems/toeplitz-matrix/
# every diagonal from top-left to bottom-right has the same element.

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # dgnal starting from el in first row
        i = 0
        j = 0
        dgnal = []
        for k in range(len(matrix[0])):
            while i < len(matrix) and j < len(matrix[0]):
                dgnal.append(matrix[i][j])
                if len(set(dgnal)) > 1: return False
                i, j = i+1, j+1
            dgnal = []
            i, j = 0, 1
            j += k
            
        # dgnal starting from el in first col
        i = 1
        j = 0
        dgnal = []
        for k in range(len(matrix)):
            while i < len(matrix) and j < len(matrix[0]):
                dgnal.append(matrix[i][j])
                if len(set(dgnal)) > 1: return False
                i, j = i+1, j+1
            dgnal = []
            i, j = 1, 0
            i += k
            
        return True
        
if __name__=="__main__":
    obj = Solution()
    param_1 = obj.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
    print(param_1)

# better solution
class Solution:
    def isToeplitzMatrix(self, m):
            for i in range(len(m) - 1):
                for j in range(len(m[0]) - 1):
                    if m[i][j] != m[i + 1][j + 1]:
                        return False
            return True