class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        row, col = len(grid), len(grid[0])
        r, c = row - 1, 0 

        while r >= 0 and c < col:
            if grid[r][c] < 0:
                count += col - c 
                r -= 1
            else:
                c += 1
        return count 