class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)

        if r <= 0:
            return 0

        while l < r:
            if nums[l] == val:
                r -= 1
                temp = nums[l] 
                nums[l] = nums[r]
                nums[r] = temp 
                
            else:
                l += 1

        return r