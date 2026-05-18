class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxProd = nums[0]
        # n = len(nums)

        # for i in range(n):
        #     mul = 1
        #     for j in range(i, n):
        #         mul *= nums[j]
        #         maxProd = max(maxProd, mul)
        
        # return maxProd

        currMax = nums[0]
        currMin = nums[0]
        maxProd = nums[0]
        n = len(nums)

        for i in range(1, n):
            temp = max(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMax = temp
            maxProd = max(maxProd, currMax)
        return maxProd