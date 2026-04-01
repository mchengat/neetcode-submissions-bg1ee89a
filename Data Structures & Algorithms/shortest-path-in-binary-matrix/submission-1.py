class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid is None or grid[0] is None or grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        visited = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = collections.deque()
            q.append((row, col, 1))
            visited.add((row, col))
            grid[row][col]=1
            while q:
                r, c, length = q.popleft()
                if r == n-1 and c==n-1:
                        return length
                directions = [(-1,0),(1,0), (0,1), (0,-1), (1,-1), (-1,1), (-1,-1), (1,1)]
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if 0<=row<n and 0<=col<n and grid[row][col]==0:
                        q.append((row,col,length+1))
                        grid[row][col]=1
            return -1


        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 0:
        #             shortest_path = bfs(row, col)

        return bfs(0,0)