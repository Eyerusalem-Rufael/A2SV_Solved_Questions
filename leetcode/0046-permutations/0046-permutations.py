class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        arr = []
        comb = []
        def pair(num):
            if len(comb) == len(nums):
                arr.append(comb[:])
                return 

            for num in nums:
                if num not in comb:
                    comb.append(num)
                    pair(comb)
                    comb.pop()

        pair([])
        return arr