class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return target in matrix[mid] 
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False