class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        arr = []
        def back(start,comb):
            if len(comb) > 1:
                arr.append(comb[:])
            seen = set()
            for i in range(start,len(nums)):
                if nums[i] in seen:
                    continue
                if not comb or comb[-1] <= nums[i]:
                    seen.add(nums[i])
                    comb.append(nums[i])
                    back(i+1,comb)
                    comb.pop()
            return

        back(0,[])
        return arr