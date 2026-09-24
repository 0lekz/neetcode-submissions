class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(target, row):
            L, R = 0, len(row) - 1
            while L <= R:
                mid = (L + R) // 2
                if target == row[mid]:
                    return True
                elif target < row[mid]:
                    R = mid - 1
                elif target > row[mid]:
                    L = mid + 1
            return False

        # what we could do is call this on each row, but that would be O(m * log(n)), a better solution would be to use
        # binary search to find a row in which target might be judging by boundaries of such row
        # easiest way would be to compare last elements of each row and as soon as target < matrix[i][-1] we call search on that row
        
        # basically also binary search but with additional condition, if it's < matrix[mid][-1] it should also be > matrix[mid][0] if it's not go next
        U, D = 0, len(matrix) - 1
        while U <= D:
            mid = (U + D) // 2
            if target < matrix[mid][-1]:
                if target >= matrix[mid][0]:
                    return search(target, matrix[mid])
                else: 
                    D = mid - 1
            elif target > matrix[mid][-1]:
                U = mid + 1
            elif target == matrix[mid][-1]:
                return True
        return False