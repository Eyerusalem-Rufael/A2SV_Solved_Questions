class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        heights.append(0) #act as a fake block
        max_rect = 0

        for idx , num in enumerate(heights): 
            while stk and heights[stk[-1]] > num: #monoincreasing
                height = heights[stk.pop()]
                if not stk:
                    width = idx
                else:
                    width = idx - stk[-1] - 1 #rightsmaller - leftsmaller - 1 between them
                area = height * width
                max_rect = max(max_rect , area)
            stk.append(idx)
        return max_rect