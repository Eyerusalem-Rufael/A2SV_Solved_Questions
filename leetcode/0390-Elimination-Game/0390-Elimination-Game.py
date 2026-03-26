class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(first , gap , remain , direction):
            if remain < 2: #base-case
                return first
            increment = gap if direction or remain  % 2 else 0 #odd R->L
            return helper(first + increment ,gap * 2 , remain // 2, not direction)  

        return helper(1,1,n,True) #inital