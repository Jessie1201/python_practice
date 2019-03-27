# https://leetcode.com/problems/rotting-oranges/
# minimum number of minutes that must elapse until no cell has a fresh orange

class Solution:
    def orangesRotting(self, grid) -> int:
        def isRotten(grid) -> bool:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return False
            return True

        if all(grid[i][j] != 1 for i in range(len(grid)) for j in range(len(grid[0]))):
            return 0
        
        if all(grid[i][j] != 2 for i in range(len(grid)) for j in range(len(grid[0]))):
            return -1

        maximum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maximum += 1
        
        t = 0
        while not isRotten(grid) and t <= maximum:
            new = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        if i-1>=0 and grid[i-1][j] == 1:
                            new[i-1][j] = 2
                        if i+1<len(grid) and grid[i+1][j] == 1:
                            new[i+1][j] = 2
                        if j-1>=0 and grid[i][j-1] == 1:
                            new[i][j-1] = 2
                        if j+1<len(grid[0]) and grid[i][j+1] == 1:
                            new[i][j+1] = 2
            t += 1
            grid = [[new[x][y] for y in range(len(new[0]))] for x in range(len(new))]
        return t if t < maximum else -1

                
        



if __name__=="__main__":
    obj = Solution()
    param_1 = obj.orangesRotting([[2],[2],[1],[0],[1],[1]])
    print(param_1)
