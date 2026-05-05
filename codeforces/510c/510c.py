from collections import defaultdict, deque
n = int(input())
names = [input() for i in range(n)]
graph = defaultdict(list)
indegree = {chr(ord('a') + i) : 0 for i in range(26)}
for i in range(n-1):
    word1 = names[i]
    word2 = names[i+1]
    for j in range(min(len(word1),len(word2))):
        if word1[j] != word2[j]:
            if word2[j] not in graph[word1[j]]:
                graph[word1[j]].append(word2[j])
                indegree[word2[j]] += 1
            break

    else:
        if len(word1) > len(word2):
            print('Impossible')
            exit()
            
res = []
queue = deque()
for letter in indegree:
    if indegree[letter] == 0:
        queue.append(letter)
while queue:
    node = queue.popleft()
    res.append(node)
    for neigh in graph[node]:
        indegree[neigh] -= 1
        if indegree[neigh] == 0:
            queue.append(neigh)

if len(res) == 26: #cheking if cycle is detected
    print(''.join(res))
else:
    print('Impossible')