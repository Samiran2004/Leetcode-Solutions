class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        prefArr = [0] * (n + 1)

        for i in range(n):
            prefArr[i + 1] = prefArr[i] + (1 if nums[i] == target else -1)
        
        ans = 0

        for l in range(n):
            for r in range(l, n):
                if prefArr[r + 1] - prefArr[l] > 0:
                    ans += 1
        
        return ans