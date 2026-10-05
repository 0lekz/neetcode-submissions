class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search rotated array

        # naive solution, could look for index of min element
        # and start left pointer from it, and right pointer would be
        # (left + len(nums)) % len(nums) but in this case we spend O(n) to find
        # min element, and log(n) on binary search after.
        # Maybe there is better solution in log(n) time not n

        # obviously binary search itself is easy, the question is to how we select
        # left and right pointers.

        # use binary search to find at what point we jump from max to min
        # it's also the only index in which nums[i] > nums[i+1]

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        cutid = l
        # now that we know the cut, simply:

        l, r = 0, len(nums) - 1

        if target >= nums[cutid] and target <= nums[r]:
            l = cutid
        else:
            r = cutid - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1

