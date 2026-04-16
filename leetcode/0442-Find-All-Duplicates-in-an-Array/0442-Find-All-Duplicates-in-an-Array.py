from collections import defaultdict
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            swap_idx = nums[i] - 1
            if nums[i] != nums[swap_idx]:
                nums[i] , nums[swap_idx] = nums[swap_idx] , nums[i]
            else:
                i += 1
        #print(nums)
        arr = []
        for i in range(n):
            if nums[i] != i + 1:
                arr.append(nums[i])
        return arr