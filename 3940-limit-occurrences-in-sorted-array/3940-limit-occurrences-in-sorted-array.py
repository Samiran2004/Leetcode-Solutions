class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []

        for x in nums:
            if len(res) < k or res[-k] != x:
                res.append(x)
        return res