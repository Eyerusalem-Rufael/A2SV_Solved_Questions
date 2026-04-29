class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        ancestor = [set() for _ in range(n)]
        queue = deque()
        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i) 
        while queue:
            node = queue.popleft()
            for neigh in graph[node]:
                ancestor[neigh].add(node)
                ancestor[neigh].update(ancestor[node])
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh) 

        return [sorted(list(ancestor[i])) for i in range(n)]