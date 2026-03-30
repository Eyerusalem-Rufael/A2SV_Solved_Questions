class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        comb = []
        def back(start,end):
            if len(comb) <= len(nums):
                arr.append(comb[:])
                
            for i in range(start,end):
                comb.append(nums[i])
                back(i+1,end)
                comb.pop()

        back(0,len(nums))
        return arr