class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums) 
        prev = nums[-1] 
        count = 0

        for i in range(n-2,-1,-1):
            if nums[i] > prev:
                partitions= ceil(nums[i] / prev)
                count += partitions- 1
                prev = nums[i] // partitions
            else:
                prev = nums[i]

        return count

        