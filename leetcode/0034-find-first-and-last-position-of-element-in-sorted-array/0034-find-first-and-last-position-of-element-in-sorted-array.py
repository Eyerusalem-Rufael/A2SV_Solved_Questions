class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def helper(search):
            idx = -1
            left = 0
            right = len(nums)-1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    idx = mid
                    if search:
                        right = mid -1
                    else:
                        left = mid + 1

            return idx

        left_search = helper(True)
        right_search = helper(False)

        return [left_search,right_search]