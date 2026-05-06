from collections import defaultdict, deque
t = int(input())
for _ in range(t):
    n = int(input())
    gives = list(map(int,input().split()))
    indegree = [0] *(n+1)
    graph = defaultdict(list)
    queue = deque()
    for i in range(1,n+1):
        graph[i].append(gives[i-1])
        indegree[gives[i-1]] += 1
    # print(indegree) [0, 1, 2, 1, 1, 0]

    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append((i,1)) #spider and depth
    max_yr = 0
    while queue:
        node,yr = queue.popleft()
        max_yr = max(yr,max_yr)
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append((neigh,yr + 1))
    print(max_yr + 2) #intial and stable