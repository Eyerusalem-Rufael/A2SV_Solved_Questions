class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = []
        curr_min = nums[0] 
        for num in nums:
            while stk and num >= stk[-1][0]: #monotonic stack decreasing
                stk.pop()
            if stk and num > stk[-1][1]: #compare it to the min nums[i] and nums[k]
                return True

            stk.append((num,curr_min)) #append the max and min stk(max,min)
            curr_min = min(curr_min,num)

        return False