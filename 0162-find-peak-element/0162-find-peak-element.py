class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            left, right = True, True

            if i > 0 and nums[i] <= nums[i - 1]:
                left = False
            if i < n - 1 and nums[i] <= nums[i + 1]:
                right = False
            
            if left and right:
                return i