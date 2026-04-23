class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def inbound(r,c):
            return 0 <= r < rows and  0 <= c < cols
        def dfs(r,c,visited):
            visited.add((r,c))
            for new_r,new_c in direction:
                new_r += r
                new_c += c
                if inbound(new_r,new_c) and (new_r,new_c) not in visited and heights[new_r][new_c] >= heights[r][c]: 
                    dfs(new_r,new_c,visited)

        direction = [(0,1),(0,-1),(-1,0),(1,0)]
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        visited = set()

        for r in range(rows):
            dfs(r,0,pacific)
            dfs(r,cols-1,atlantic)
        for c in range(cols):
            dfs(0,c,pacific)
            dfs(rows-1,c,atlantic)

        return list(pacific&atlantic)