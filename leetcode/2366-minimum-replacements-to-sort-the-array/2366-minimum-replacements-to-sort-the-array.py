class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums) 
        limit = nums[-1] 
        count = 0

        for i in range(n-2,-1,-1):
            if nums[i] > limit:
                partitions = ceil(nums[i] / limit)
                count += partitions- 1
                limit = nums[i] // partitions
            else:
                limit = nums[i]

        return count

        