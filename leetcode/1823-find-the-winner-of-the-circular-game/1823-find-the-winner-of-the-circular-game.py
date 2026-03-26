class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def player(n):
            if n == 1:
                return 0 #of the player is 1 the one in the idx 0 is the winner
            return (player(n - 1) + k) % n
        return player(n) + 1
