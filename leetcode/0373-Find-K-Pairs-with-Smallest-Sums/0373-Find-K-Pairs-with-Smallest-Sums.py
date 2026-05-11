class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []
        n , m = len(nums1) , len(nums2)
        for i in range(n):
            heapq.heappush(heap,(nums1[i] + nums2[0],i,0))

        while heap and len(ans) < k:
            val,row,col = heapq.heappop(heap)
            ans.append([nums1[row],nums2[col]])
            if col + 1 < m:
                heapq.heappush(heap,(nums1[row] + nums2[col+1],row,col+1))


        return ans