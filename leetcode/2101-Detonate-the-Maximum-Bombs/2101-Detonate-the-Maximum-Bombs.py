class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(i+1,n):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[j]

                distance = sqrt((x1-x2)**2 + (y1 - y2)**2)
                if distance <= r1: #i can include j
                    graph[i].append(j)
                if distance <= r2:  
                    graph[j].append(i)
        # print(graph)
        def dfs(node,visited):
            if node in visited:
                return 0
            visited.add(node)
            for neigh in graph[node]:
                dfs(neigh,visited)
            return len(visited)
        ans = 0
        for i in range(n):
            ans = max(ans,dfs(i,set()))
        return ans