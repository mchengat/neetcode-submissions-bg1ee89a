class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if grid is None or grid[0] is None:
            return 0

        maxArea = 0

        def dfs(r, c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area=1

            area+=dfs(r+1, c)
            area+=dfs(r-1, c)
            area+=dfs(r, c+1)
            area+=dfs(r, c-1)
            return area
            

        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    current_max = dfs(row, col)
                    maxArea = max(current_max, maxArea)
        return maxArea
                