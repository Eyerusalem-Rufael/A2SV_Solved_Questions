class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0,0,0]
        for num in nums:
            bucket[num] += 1
            
        idx = 0
        for i in range(len(bucket)):
            for _ in range(bucket[i]):
                nums[idx] = i
                idx += 1