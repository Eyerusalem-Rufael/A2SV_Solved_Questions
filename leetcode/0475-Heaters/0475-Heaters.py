class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)
        max_r = 0
        
        for house in houses:
            left_most = bisect_left(heaters,house) #to get the first lower bound of the house
            #search from the left and right of the picked idx this reduce the traversing  
            right = float('inf')
            if left_most < n: 
                right = heaters[left_most] - house
            
            left = float('inf')
            if left_most > 0:
                left = house - heaters[left_most - 1]  

            minimum = min(left,right)
            max_r = max(max_r,minimum)

        return max_r