class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r,c):
            return 0 <= r < row and 0 <= c < col
        def dfs(r,c):
            if not inbound(r,c) or grid[r][c] != '1':
                return 
            grid[r][c] = '0'
            for new_r , new_c in directions:  
                new_r += r
                new_c += c   
                dfs(new_r,new_c)
                
        row = len(grid)
        col = len(grid[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)
        return island