class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            swap_idx = nums[i] - 1
            if nums[i] != nums[swap_idx]:
                nums[i] , nums[swap_idx] = nums[swap_idx] , nums[i]
            else:
                i += 1
                
        return nums[-1]