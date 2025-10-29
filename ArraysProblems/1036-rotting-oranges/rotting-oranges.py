class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time, fresh = 0, 0 
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0: 
            for i in range(len(q)):
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1],[0,-1]]
                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc 
                    if (nr not in range(rows) or 
                        nc not in range(cols) or 
                        grid[nr][nc]!= 1):
                        continue 
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))
            time += 1
        return time if fresh == 0 else -1 