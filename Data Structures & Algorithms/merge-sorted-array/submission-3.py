class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1 
        count = 0

        # nums1 = [1, 3, 5, 0, 0]
        # nums2 = [2, 4] 
        while j >= 0:
            if i < 0:
                nums1[:j+1] = nums2[:j+1]
                break
            if nums1[i] > nums2[j]:
                nums1[(m + n - 1) - count] = nums1[i]
                i = i - 1
                count += 1
            else:
                nums1[(m + n - 1) - count] = nums2[j]
                j = j - 1
                count += 1

        # should be O(n + m) time and O(1) extra space
