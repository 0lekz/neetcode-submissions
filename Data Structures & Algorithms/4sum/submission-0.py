class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                L = j + 1
                R = len(nums) - 1

                while L < R: 
                    twoSum = nums[i] + nums[j]

                    if nums[L] + nums[R] + twoSum < target:
                        L += 1
                        
                    elif nums[L] + nums[R] + twoSum > target:
                        R -= 1

                    # if total == target
                    else:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        while nums[L] == nums[L - 1] and L < R:
                            L += 1
                        while nums[R] == nums[R + 1] and L < R:
                            R -= 1

        return res