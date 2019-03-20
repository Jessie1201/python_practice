# https://leetcode.com/problems/flood-fill/
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of 
# the flood fill, and a pixel value newColor, "flood fill" the image.

class Solution:
    def __init__(self):
        self.visited = []
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        src_color = image[sr][sc]
        image[sr][sc] = newColor
        self.visited.append([sr, sc])
        # up
        if sr-1 >= 0 and [sr-1,sc] not in self.visited and image[sr-1][sc] == src_color:
            self.floodFill(image, sr-1, sc, newColor)
        # down
        if sr+1 < len(image) and [sr+1,sc] not in self.visited and image[sr+1][sc] == src_color:
            self.floodFill(image, sr+1, sc, newColor)
        # left
        if sc-1 >= 0 and [sr,sc-1] not in self.visited and image[sr][sc-1] == src_color:
            self.floodFill(image, sr, sc-1, newColor)
        # right
        if sc+1 < len(image[0]) and [sr,sc+1] not in self.visited and image[sr][sc+1] == src_color:
            self.floodFill(image, sr, sc+1, newColor)
        return image


if __name__=="__main__":
    obj = Solution()
    # param_1 = obj.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    # param_1 = obj.floodFill([[0,0,0],[1,0,0]], 1, 1, 1)
    # param_1 = obj.floodFill([[1,0,0],[1,0,0]], 1, 1, 1)
    # param_1 = obj.floodFill([[0,0,0],[0,0,1]], 0, 0, 2)
    param_1 = obj.floodFill([[0,0,0],[0,0,0]], 1, 0, 2)
    print(param_1)