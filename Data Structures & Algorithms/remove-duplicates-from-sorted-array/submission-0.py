class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 1
        while R < len(nums):
            if nums[L] != nums[R]:
                L += 1
                nums[L] = nums[R]
            R += 1
        
        return L + 1


            