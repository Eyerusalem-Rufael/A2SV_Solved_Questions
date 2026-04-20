t = int(input())
for _ in range(t):
    n = int(input())
    leaf = list(map(int,input().split()))
    count = 0

    def merge(left,right):
        global count
        if left is None or right is None:
            return None
        min_left,max_left = left
        min_right,max_right = right

        if max_left < min_right: #correct ord
            return (min_left,max_right)
        elif min_left > max_right: #swap
            count += 1
            return (min_right,max_left)
        else:
            return None

    def mergsort(leaf):
        if len(leaf) <= 1:
            return (leaf[0] , leaf[0]) #min  and max
        mid = len(leaf) // 2
        left = mergsort(leaf[:mid])
        right = mergsort(leaf[mid:])

        return merge(left,right)
    
    ans = mergsort(leaf)
    print(count if ans else -1)