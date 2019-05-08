# https://leetcode.com/problems/number-of-islands/
#  graph problem, number of islands
# typical dfs, depth-first search

class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])

        def dfs(i, j):
            if 0 <= i < row and 0 <= j < column and grid[i][j] == '1':
                grid[i][j] = '#'
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count

if __name__=="__main__":
    obj = Solution()
    param_1 = obj.numIslands([["0","1","0"],["1","0","1"],["0","1","0"],["1","0","1"]])
    print(param_1)