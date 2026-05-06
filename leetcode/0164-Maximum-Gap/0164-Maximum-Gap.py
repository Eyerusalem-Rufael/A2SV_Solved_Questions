class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        #The pigeonhole principle states that if items (pigeons) are put into containers (pigeonholes)  (more items than containers), then at least one container must contain more than one item. Maximum gap ≥ average gap
        n = len(nums)
        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0

        bucket_size = (max_val - min_val) / (n-1) #there are n-1 gaps b/n buckets
        bucket = [[float('inf'),float('-inf')]for i in range(n-1)] #min , max of bucket
        for num in nums:
            if num == max_val:
                continue
            bucket_idx = int((num - min_val)/bucket_size)
            bucket[bucket_idx][0] = min(bucket[bucket_idx][0],num)
            bucket[bucket_idx][1] = max(bucket[bucket_idx][1],num)
        # print(bucket)
        max_gap = 0
        prev_max = min_val
        for i in range(n-1):
            curr_min1,curr_max1 = bucket[i]
            if curr_min1 == float(inf):
                continue
            max_gap = max(max_gap,curr_min1 - prev_max)
            prev_max = curr_max1
        return max(max_gap,max_val - prev_max)