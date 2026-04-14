from collections import Counter
t = int(input())
for _ in range(t):
    n,l,r = map(int,input().split())
    colors = list(map(int,input().split()))
    left_pair = Counter(colors[:l])
    right_pair = Counter(colors[l:])
    #check for matching
    for i in list(left_pair.keys()):
        remove = min(left_pair[i],right_pair[i])
        left_pair[i] -= remove
        right_pair[i] -= remove
        l -= remove
        r -= remove
    #make the left side greater
    if l < r:
        l,r = r,l
        left_pair,right_pair = right_pair,left_pair
    ans = 0
    transfer = (l - r) // 2
    for i in left_pair:
        while transfer >= 1 and left_pair[i] >= 2:
            left_pair[i] -= 2
            transfer -= 1
            ans += 1
    #transfered left from the duplicate move and color
    ans += transfer * 2

    #if unmatched left
    ans += r

    print(ans)