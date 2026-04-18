class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k
        def quicksort(nums,low,high):
            #basecase
            if low >= high: # nothing to swap
                return nums[k]

            start = low
            end = high
            mid = (start + end) // 2
            pivot = nums[mid]
            while start <= end:
                while nums[start] < pivot:
                    start += 1
                while nums[end] > pivot:
                    end -= 1
                if start <= end:
                    nums[start] , nums[end] = nums[end] , nums[start]
                    start += 1
                    end -= 1
            if k <= end:#go to the left
               return quicksort(nums,low,end)
            elif k >= start:
               return quicksort(nums,start,high)
            else:
                return nums[k]

        return quicksort(nums,0,n-1)