import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_stone = [-stone for stone in stones]
        heapq.heapify(max_stone)
        # print(max_stone)
        while len(max_stone) > 1:
            first = -heapq.heappop(max_stone)
            second = -heapq.heappop(max_stone)

            if first != second:
                heapq.heappush(max_stone,-(first-second))

        return -max_stone[0] if max_stone else 0