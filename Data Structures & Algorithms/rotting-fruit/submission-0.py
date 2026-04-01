class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None or grid[0] is None:
            return
        
        fresh=0
        q = collections.deque()

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh+=1

        if fresh == 0:
            return 0
        minutes = 0
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    r, c = row+dr, col+dc

                    if 0<=r<rows and 0<=c<cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh-=1
            minutes+=1

        
        return -1 if fresh != 0 else minutes-1
