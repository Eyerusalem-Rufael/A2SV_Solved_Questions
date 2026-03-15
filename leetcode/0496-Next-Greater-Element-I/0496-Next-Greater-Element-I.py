class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = defaultdict(lambda : -1)
        stk = []

        for num in nums2:
            while stk and stk[-1] < num: #monodecr if the top smaller pop it
                res[stk[-1]] = num
                stk.pop()
            stk.append(num)

        return [res[num] for num in nums1]