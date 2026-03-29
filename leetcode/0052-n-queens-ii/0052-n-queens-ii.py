class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_dia = set()
        neg_dia = set()
        board = [['.'] * n for _ in range(n)]
        res = []
        def helper(row):
            if row == n:
                res.append(["".join(row) for row in (board)])
                return
            for col in range(n):
                if col in cols or (row + col) in  pos_dia or (row - col) in  neg_dia:
                    continue
                #place
                cols.add(col)
                pos_dia.add(row + col)
                neg_dia.add(row - col)
                board[row][col] = 'Q'
                #explore
                helper(row + 1)
                #undone
                cols.remove(col)
                pos_dia.remove(row + col)
                neg_dia.remove(row - col)
                board[row][col] = '.'

        helper(0)
        return len(res)