class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1

        for i in range(0, n, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        
        return nums[n]