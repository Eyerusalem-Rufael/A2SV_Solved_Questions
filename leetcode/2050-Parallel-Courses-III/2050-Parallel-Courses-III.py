class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        max_time = [0] * n 
        graph = [[] for _ in range(n)]
        indegree = [0] * n 
        queue = deque()
    
        for u,v in relations:
            graph[u-1].append(v-1)
            indegree[v-1] += 1
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                max_time[i] = time[i]

        while queue:
            course = queue.popleft()
            for neigh in graph[course]:
                max_time[neigh] = max(max_time[neigh],max_time[course] + time[neigh])
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        return max(max_time)