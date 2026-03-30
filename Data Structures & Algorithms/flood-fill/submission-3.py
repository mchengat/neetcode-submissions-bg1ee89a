class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # m, n = len(image), len(image[0])
        # origcolor = image[sr][sc]
        # if origcolor == newColor:
        #     return image
        
        # queue = deque([(sr, sc)])
        # image[sr][sc] = newColor
        
        # while queue:
        #     r,c = queue.popleft()
        #     for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
        #         nr, nc = r + dr, c + dc
        #         if 0<=nr<m and 0<=nc<n and image[nr][nc] == origcolor:
        #             image[nr][nc] = newColor
        #             queue.append((nr, nc))
        
        # return image

        m, n = len(image), len(image[0])
        origColor = image[sr][sc]
        if origColor == newColor:
            return image

        def dfs(r: int, c: int):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != origColor:
                return
            image[r][c] = newColor
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image