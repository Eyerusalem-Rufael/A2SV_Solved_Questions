from collections import defaultdict, deque
n = int(input())
graph = defaultdict(list)
if n == 1:
    print(0)
    exit()

for _ in range(n-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
def bfs(start):
    queue = deque([(start,0)]) # node,further distance
    visited = set([start])
    further_distance = 0
    further_node = start
    while queue:
        node,distance = queue.popleft()
        if further_distance < distance :
            further_distance = distance
            further_node = node
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append((neigh,distance + 1))

    return further_node,further_distance
node_a , _ = bfs(1)
node_b, diameter = bfs(node_a)
circumference = 3 * diameter
print(circumference)