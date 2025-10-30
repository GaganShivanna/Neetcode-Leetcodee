class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color:
            return image
        
        #DFS helper function 
        def dfs(r,c):
            if ( r not in range(rows) or 
                 c not in range(cols) or 
                 image[r][c]!= oldColor):
                 return 
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        dfs(sr,sc)
        return image