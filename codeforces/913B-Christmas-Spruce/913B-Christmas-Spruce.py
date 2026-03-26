vertices = int(input())
nodes = [[] for _ in range(vertices+1)]

for i in range(2,vertices+1):
    parent = int(input())
    nodes[parent].append(i)

#print(nodes)
for i in range(1,vertices+1):
    if len(nodes[i]) > 0: # we got nonleaf
        leaf = 0
        for child in nodes[i]:
            if len(nodes[child]) == 0:
                leaf += 1
        if leaf < 3:
            print('No')
            exit()
else:
    print('Yes')