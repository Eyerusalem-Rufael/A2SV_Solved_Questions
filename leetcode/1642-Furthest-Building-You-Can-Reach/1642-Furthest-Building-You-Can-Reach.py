class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        max_heap = []
        for i in range(n - 1):
            difference = heights[i+1] - heights[i]
            if difference < 0:
                continue
            heapq.heappush(max_heap,-difference)
            bricks -= difference
            if bricks < 0:
                largest = - heapq.heappop(max_heap)
                bricks += largest
                ladders -= 1

            if ladders < 0:
                return i

        return n - 1