class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        DIRECTIONS = [[0,1],[1,0],[-1,0],[0,-1]]

        def bfs(row, col):
            q = deque()
            grid[row][col] = 0
            q.append((row, col))
            cur_area = 0
            while q:
                ro, co = q.popleft()
                cur_area += 1
                for dr, dc in DIRECTIONS:
                    nr, nc = ro + dr, co + dc
                    if nr < 0 or nc < 0 or nr == m or nc == n or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
            return cur_area

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area
        