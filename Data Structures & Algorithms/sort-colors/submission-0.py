class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0] # for red, white and blue

        for num in nums:
            counts[num] += 1

        idx = 0
        for num in range(len(counts)):
            for _ in range(counts[num]):
                nums[idx] = num
                idx += 1
        return nums
