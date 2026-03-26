class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []
        comb = []
        def pair(num):
            if len(comb) == k:
                arr.append(comb[:])
                return 

            for i in range(num,n+1):
                comb.append(i)
                pair(i+1)
                comb.pop()

        pair(1)
        return arr