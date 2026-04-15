class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first section find the row with the bounds left <= target <= right

        row = -1

        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                row = mid
                break

            elif matrix[mid][-1] < target:
                lo = mid + 1
            
            else:
                hi = mid - 1
        
        if row == -1: return False

        lo = 0
        hi = len(matrix[row]) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if matrix[row][mid] == target:

                return True

            elif matrix[row][mid] < target:
                lo = mid + 1
            
            else:
                hi = mid - 1
        
        return False