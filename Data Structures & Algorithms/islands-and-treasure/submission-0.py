from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #wave bfs! go through all treasures at once after finding them
        seen=set()
        DIRECTIONS = [[0,1],[1,0],[0,-1],[-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])
        treasure=deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    treasure.append([r,c])
                    seen.add((r,c))
        dist=0
        while treasure:
            for i in range(len(treasure)):
                r, c = treasure.popleft()
                grid[r][c] = dist
                for dr, dc in DIRECTIONS:
                    row=dr+r
                    col=dc+c
                    if row>(ROWS-1) or col>(COLS-1) or row<0 or col<0 or grid[row][col]==-1 or (row,col) in seen:
                        continue
                    seen.add((row,col))
                    treasure.append([row,col])
            dist+=1
                
            
            
        
        """
        #find islands first and then their distance to treasure (and continue to update if we find a better min)
        #basically find all treasure, then bfs or dfs from there to set every reachable piece of land to the minimum of its current value vs the recursion depth    
        #O(m*n) time, O(m*n) space
        directions = [[0, 1], [1,0],[-1,0],[0,-1]] # to make BFS code a lil easier
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r: int, c: int, depth: int):
            seen=set() #create a seen for every iteration of bfs
            q=deque()
            q.append((r,c,depth))
            while q:
                row, col, dep = q.popleft()
                if (row,col) in seen:
                    continue
                for dr, dc in directions:
                    #add the indices
                    #calculate indices
                    if (dr+row)<0 or (dc+col)<0 or (dr+row)>=ROWS or (dc+col)>=COLS or grid[(dr+row)][(dc+col)]== -1:
                        continue
                    grid[dr+row][dc+col]=depth+1
                    bfs((dr+row),(dc+col), depth+1)
                

            

        for i, row in enumerate(grid):
            for j, element in enumerate(row):
                if element == 0: #found treasure
                    bfs(i,j,0)
        return grid
        """
