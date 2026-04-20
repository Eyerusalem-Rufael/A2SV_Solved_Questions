class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        def merge(left,right):
            right_count = 0
            i = j = 0
            res = []
            n = len(left)
            m = len(right)
            while i < n and j < m:
                if left[i][0] <= right[j][0]:
                    count[left[i][1]] += right_count
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    right_count += 1
                    j += 1
            while i < n:
                count[left[i][1]] += right_count
                res.append(left[i])
                i += 1
            res.extend(right[j:])
            return res

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left,right)

        index = [(val,idx) for idx,val in enumerate(nums)]
        mergesort(index)
        return count