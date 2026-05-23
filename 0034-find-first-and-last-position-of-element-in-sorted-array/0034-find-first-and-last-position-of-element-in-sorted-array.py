import bisect

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        lower_bound = bisect.bisect_left(nums, target)

        if lower_bound == len(nums) or nums[lower_bound] != target:
            return [-1, -1]
            
        upper_bound = bisect.bisect_right(nums, target) - 1
        
        return [lower_bound, upper_bound]