class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def min_force(mid):
            count = 1
            idx = 0
            while count < m:
                target = position[idx] + mid
                nxt = bisect_left(position,target) #the first elt that is  >= target
                if nxt == len(position):
                    return False
                idx = nxt
                count += 1
            return True

        low = 1
        high = max(position)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if min_force(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans