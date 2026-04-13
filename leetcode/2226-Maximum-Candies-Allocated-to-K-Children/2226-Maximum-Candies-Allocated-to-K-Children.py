class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def help(mid):
            count = 0
            for i in candies:
                count += i // mid
            return count

        low = 1
        high = max(candies)
        while low <= high:
            mid = (high + low) // 2
            candy = help(mid)
            if candy < k:
                high = mid - 1
            else:
                low = mid + 1

        return high