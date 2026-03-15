class Solution:
    def minOperations(self, nums: List[int]) -> int:
        queue = deque()
        count = 0
        n = len(nums)
        
        for idx in range(n):
            while queue and queue[0] < idx - 2:
                queue.popleft()

            parity = (nums[idx] + len(queue)) % 2
            if not parity:
                if idx + 2 >= n:
                    return -1
                    
                count += 1
                queue.append(idx)

        return count