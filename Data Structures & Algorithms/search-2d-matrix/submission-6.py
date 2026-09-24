class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # one pass binary search. Treat matrix as a flattened matrix or one big sorted array

        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = (l + r) // 2
            # map back to row and col
            row = mid // COLS
            col = mid % COLS

            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                # found target
                return True
        return False