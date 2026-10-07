from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #try bfs... we dont need a seen set just set it to -
        
        islands=0

        ROWS=len(grid)
        COLS=len(grid[0])
        DIRECTIONS = [[-1,0],[0,-1],[1,0],[0,1]]

        def bfs(r,c):
            q=deque()
            grid[r][c]="0"
            q.append((r,c))
            while q:
                ro, co = q.popleft()
                
                for dr, dc in DIRECTIONS:
                    row=dr+ro
                    col=dc+co
                    if min(row,col) <0 or row==ROWS or col==COLS or grid[row][col] == "0":
                        continue
                    #otherwise we found land!
                    q.append((row,col))
                    grid[row][col]="0"




        #do bfs on islands we haven't seen before
        for i, r in enumerate(grid):
            for j, c in enumerate(grid[0]):
                if grid[i][j]=="1":
                    bfs(i,j)
                    islands+=1
                
                
        return islands




        #union find?
        #when 2 land cells are adjacent, merge them

        




        """
        #must be at least O(n^2) time complexity since we must examine every index
        #we could maybe pad arrays with zeros
        seen=set() #use a hash set to store tuples of indices we've already visited
        islands=0
        def dfs(i, j):

            if grid[i][j] == 0:
                return 


        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if (i, j) in seen:
                    continue
"""
                




        
        