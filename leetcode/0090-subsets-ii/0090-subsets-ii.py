class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        comb = []
        def back(start):
            arr.append(comb[:])
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                comb.append(nums[i])
                back(i+1)
                comb.pop()

        back(0)
        return arr