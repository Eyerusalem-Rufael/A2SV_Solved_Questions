class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        left = right = 0 
        max_size = 0
        n = len(nums)

        for right in range(n):
            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            min_q.append(nums[right])

            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
            max_q.append(nums[right])

            while max_q[0] - min_q[0] > limit:
                num = nums[left]
                if num == max_q[0]:
                    max_q.popleft()

                if num == min_q[0]:
                    min_q.popleft()

                left += 1

            max_size = max(max_size , right - left + 1)

        return max_size