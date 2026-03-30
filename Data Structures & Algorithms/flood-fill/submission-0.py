class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # m, n = len(image), len(image[0])
        # origColor = image[sr][sc]

        # if image == origColor:
        #     return image
        
        # def dfs(r: int, c: int):
        #     if r<0 or r>=m or c<0 or c>=n or image[r][c] != origColor:
        #         return
        #     image[r][c] = color
        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)
        
        # dfs(sr, sc)
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