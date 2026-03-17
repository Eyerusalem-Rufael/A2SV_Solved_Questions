class Solution:
    def factorial(self, n: int) -> int:
            if n == 1 or n == 0:
                return n
            return n * self.factorial(n-1)

    def trailingZeroes(self, n: int) -> int:
       factorial = self.factorial(n)
       count = 0

       while factorial > 0 and factorial % 10 == 0:
            factorial //= 10
            count += 1

       return count
        
