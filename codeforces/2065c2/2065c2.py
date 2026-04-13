from bisect import bisect_left
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
 
    flag = True
    prev = float('-inf')
    for i in range(n):
        curr = a[i]
        opt= float('inf')
 
        #opt-1
        if curr >= prev:
            opt = curr
 
        #opt-2
        idx = bisect_left(b,curr + prev)
        
        if idx < m:
            opt = min(opt,b[idx] - a[i])
 
        if opt == float('inf'):
            flag = False
            break
 
        prev = opt
 
    print('YES' if flag else 'NO')