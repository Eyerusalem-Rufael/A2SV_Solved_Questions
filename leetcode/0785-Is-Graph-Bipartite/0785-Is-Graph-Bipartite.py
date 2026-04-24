class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
      n = len(graph)  
      color = [-1] * n
      def dfs(node):
        for neigh in graph[node]:
            if color[neigh] == -1:
                color[neigh] = 1 - color[node]
                if not dfs(neigh):
                    return False
            elif color[neigh] == color[node]:
                return False
        return True       

      for i in range(n):
        if color[i] == -1:
            color[i] = 1
            if not dfs(i):
                return False
                
      return True