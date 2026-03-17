class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def helper(x,n):
            if n == 0:
                return 1
            if x == 0: 
                return 0
            res = helper(x , n//2)
            if n % 2 == 0:
                return (res * res) % modulo 
            else:
                return (res * res * x) % modulo

        modulo = 10 ** 9 + 7
        even = ceil(n / 2)
        odd = floor(n / 2)
        return  (helper(5,even) * helper(4,odd)) % modulo