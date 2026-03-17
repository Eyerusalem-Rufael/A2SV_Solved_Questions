class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            res = helper(x , n//2)
            if n % 2 == 0:
                return res * res
            else:
                return res * res * x
            
        if n >= 0:
            return helper(x,abs(n))
        else:
            return 1 / helper(x,abs(n))
