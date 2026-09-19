class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Cascading 3 pointers

        zero = one = 0
        for two in range(len(nums)):
            temp = nums[two]
            nums[two] = 2
            if temp < 2: # 1 or 0
                nums[one] = 1
                one += 1
            if temp < 1: # 0
                nums[zero] = 0
                zero += 1