class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(rows-1, cols-1): 1}

        def dfs(row,col):
            if row == rows or col == cols or obstacleGrid[row][col]==1:
                return 0
            if (row, col) in dp:
                return dp[(row, col)]

            dp[(row, col)] = dfs(row+1, col) + dfs(row, col+1)
            return dp[(row, col)]
        return dfs(0,0)