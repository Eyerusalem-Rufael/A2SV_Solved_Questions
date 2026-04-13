class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def count_day(mid):
            total = 0
            count = 1

            for i in weights:
                if count > days:
                    return count

                if total + i > mid:
                    count += 1
                    total = 0
                total += i

            return count

        low = max(weights)
        high = sum(weights)
        
        while low < high:
            mid = (low + high) // 2
            need = count_day(mid)
            if  need <= days: 
                high = mid
            else:
                low = mid + 1
        
        return low