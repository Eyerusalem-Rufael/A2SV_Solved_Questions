class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        queue = deque()
        left = 0
        res = []

        for i in range(n):
            
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)  

            if i >= k - 1: #append after they hit the window size 
                res.append(nums[queue[0]]) 
                if nums[left] == nums[queue[0]]:  # wait till the window is equal to k, we r gonna check if the                                                 leftmost elt that is gonna be removed equall to the max 
                    queue.popleft() 
                left += 1

        return res