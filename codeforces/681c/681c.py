import heapq
n = int(input())
operation = []
heap = []
ans = []
for i in range(n):
    operation.append(input())
for opr in operation:
    if opr.startswith('insert'):
        x = int(opr.split()[1])
        heapq.heappush(heap,x)
        ans.append(f'insert {x}')

    elif opr.startswith('getMin'):
        x = int(opr.split()[1])
        while heap and heap[0] < x:
            heapq.heappop(heap)
            ans.append('removeMin')
        if not heap or heap[0] > x:
            heapq.heappush(heap,x)
            ans.append(f'insert {x}')
        ans.append(f'getMin {x}')

    elif opr.startswith('removeMin'):
        if not heap:
            heapq.heappush(heap,1)
            ans.append('insert 1')
        heapq.heappop(heap)
        ans.append('removeMin')

print(len(ans))
for elt in ans:
    print(elt)