class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we are looking for max Area, where
        # Area = height * lenght
        # Area = min(height[i], height[j]) * (j - i)

        # First solution that comes to mind is brute force, but then we will have 2 nested loops,
        # Thus O(N^2) time complexity

        # If we take 2 pointers and iterate throught them, only changing the min one first we can 
        # get the solution in O(N) time

        right = len(heights) - 1
        left = 0
        area = min(heights[right], heights[left]) * (right - left)
        while right > left:
            if heights[right] > heights[left]:
                left += 1
            else: right -= 1
            if area < min(heights[right], heights[left]) * (right - left):
                area = min(heights[right], heights[left]) * (right - left)
        return area