class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(r,c):
            return 0 <= r < rows and 0 <= c < cols 
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c):
            if not inbound(r,c) or board[r][c] != 'O':
                return 
            board[r][c] = "T"
            for new_r,new_c in direction:
                dfs(new_r + r, new_c + c)
             
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)


        for r in range(rows):
            for c in range(cols):
                if  board[r][c] == 'O':
                    board[r][c] = 'X'  
                elif board[r][c] == 'T':
                    board[r][c] = 'O'